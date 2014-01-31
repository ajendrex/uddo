from django.shortcuts import get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views import generic

from recursos.models import Recurso, ComentarioRecurso

def index(request):
  recursos_list = Recurso.objects.filter(creador=request.user)
  template = loader.get_template('recursos/index.html')
  context = RequestContext(request, {'recursos_list': recursos_list,})
  return HttpResponse(template.render(context))

class DetailView(generic.DetailView):
  model = Recurso
  template_name = 'recursos/detalle.html'

def comentar(request, recurso_id):
  c = get_object_or_404(Recurso, pk=recurso_id)

  if not request.user.is_authenticated():
    return redirect('/login/?next=%s' % reverse('cursos:detalle', args=(c.id,)))

  comentario = ComentarioRecurso()
  comentario.owner = request.user
  comentario.recurso = c
  comentario.comentario = request.POST['texto']
  comentario.fec_comentario = request.POST['fecha']
  comentario.save()
  return redirect(reverse('recursos:detalle', args=(c.id,)))
