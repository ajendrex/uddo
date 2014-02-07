from django.shortcuts import get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.forms.models import inlineformset_factory

from recursos.models import Recurso, ComentarioRecurso, RecursoForm, InsumoRecurso

@login_required
def index(request):
  recursos_list = Recurso.objects.filter(creador=request.user)
  template = loader.get_template('recursos/index.html')
  context = RequestContext(request, {'recursos_list': recursos_list,})
  return HttpResponse(template.render(context))

class DetailView(generic.DetailView):
  model = Recurso
  template_name = 'recursos/detalle.html'

@login_required
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

@login_required
def crearRecurso(request):
  InsumoFormset = inlineformset_factory(Recurso, InsumoRecurso)
  if request.method == 'POST':
    recursoForm = RecursoForm(request.POST)
    insumoFormset = InsumoFormset(request.POST, request.FILES)
    if recursoForm.is_valid():
      recurso = recursoForm.save(commit=False)
      recurso.creador = request.user
      recurso.save()
      for insumoForm in insumoFormset:
        if insumoForm.is_valid():
          insumoRecurso = insumoForm.save(commit=False)
          if not insumoRecurso.archivo.name:
            continue
          insumoRecurso.recurso = recurso
          insumoRecurso.save()
      return redirect(reverse('recursos:detalle', args=(recurso.id,)))
  else:
    recursoForm = RecursoForm()
    insumoFormset = InsumoFormset()

  template = loader.get_template('recursos/crearRecurso.html')
  context = RequestContext(request, {'recursoForm': recursoForm, 'insumoFormset': insumoFormset})
  return HttpResponse(template.render(context))
