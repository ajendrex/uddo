from django import template
from django.template.defaultfilters import stringfilter
from django.template import resolve_variable
from django.contrib.auth.models import Group
import os

register = template.Library()


@register.filter(name='basename')
@stringfilter
def basename(value):
  return os.path.basename(value)

@register.tag()
def ifusergroup(parser, token):
    """ Check to see if the currently logged in user belongs to a specific
    group. Requires the Django authentication contrib app and middleware.

    Usage: {% ifusergroup Admins %} ... {% endifusergroup %}

    """
    try:
        tag, group = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("Tag 'ifusergroup' requires 1 argument.")
    nodelist = parser.parse(('endifusergroup',))
    parser.delete_first_token()
    return GroupCheckNode(group, nodelist)

@register.tag()
def ifnotusergroup(parser, token):
    """ Check to see if the currently logged in user doesn't belong to a specific
    group. Requires the Django authentication contrib app and middleware.

    Usage: {% ifnotusergroup Admins %} ... {% endifnotusergroup %}

    """
    try:
        tag, group = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("Tag 'ifnotusergroup' requires 1 argument.")
    nodelist = parser.parse(('endifnotusergroup',))
    parser.delete_first_token()
    return NotGroupCheckNode(group, nodelist)
  
class GroupCheckNode(template.Node):
    def __init__(self, group, nodelist):
        self.group = group
        self.nodelist = nodelist
    def render(self, context):
        user = resolve_variable('user', context)
        if not user.is_authenticated:
            return ''
        try:
            group = Group.objects.get(name=self.group)
        except Group.DoesNotExist:
            return ''
        if group in user.groups.all():
            return self.nodelist.render(context)
        return ''

class NotGroupCheckNode(template.Node):
    def __init__(self, group, nodelist):
        self.group = group
        self.nodelist = nodelist
    def render(self, context):
        user = resolve_variable('user', context)
        if not user.is_authenticated:
            return ''
        try:
            group = Group.objects.get(name=self.group)
        except Group.DoesNotExist:
            return ''
        if group in user.groups.all():
            return ''
        return self.nodelist.render(context)

def key(d, key_name):
    try:
        value = d[key_name]
        print("hola mundo")
    except KeyError:
        from django.conf import settings

        value = settings.TEMPLATE_STRING_IF_INVALID

    return value
key = register.filter('key', key)
