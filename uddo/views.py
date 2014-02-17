from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext, loader
from django.http import HttpResponse

# Create your views here.
@login_required
def home(request):
  template = loader.get_template('uddo/home.html')
  context = RequestContext(request, {})
  return HttpResponse(template.render(context))
