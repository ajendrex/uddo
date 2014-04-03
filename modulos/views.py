from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.core.urlresolvers import reverse

from cursos.models import *
from modulos.models import *
from modulos.forms import *

# Create your views here.
@login_required
def detalle(request, curso_id):
  u = request.user
  objetos = {}
  curso = get_object_or_404(Curso, pk=curso_id)
  if u != curso.owner:
    objetos["mensaje_de_error"] = "No posee privilegios para ver esta página."
  else:
    objetos["modulos_list"] = Modulo.objects.filter(curso=curso).order_by("orden")
    objetos["curso"] = curso
    nuevaPaginaForms = {}
    paginaForms = {}
    for modulo in curso.modulos.all():
      nuevaPaginaForms[modulo.id] = PaginaForm(initial={'modulo':modulo})
      paginaForms[modulo.id] = {}
      for pagina in modulo.paginas.all():
        paginaForms[modulo.id][pagina.id] = PaginaForm(instance=pagina)
    objetos["nuevaPaginaForms"] = nuevaPaginaForms
    objetos["paginaForms"] = paginaForms

  template = loader.get_template('modulos/detalle.html')
  context = RequestContext(request, objetos)
  return HttpResponse(template.render(context))

@login_required
def crearModulo(request, curso_id):
  u = request.user
  curso = get_object_or_404(Curso, pk=curso_id)
  objetos = {}
  if u != curso.owner:
    objetos["mensaje_de_error"] = "No posee privilegios para crear un módulo en curso con id=." + str(curso_id)
  else:
    objetos["curso"] = curso
    if request.method == 'POST':
      moduloForm = ModuloForm(request.POST)
      if moduloForm.is_valid():
        modulo = moduloForm.save(commit=False)
        modulo.curso = curso
        modulo.orden = curso.nModulos()
        modulo.save()
        return redirect(reverse('modulos:detalle', args=(curso_id)))
      else:
        objetos["moduloForm"] = moduloForm
    else:
      objetos["moduloForm"] = ModuloForm(initial={'curso':curso_id})

  template = loader.get_template('modulos/crearModulo.html')
  context = RequestContext(request, objetos)
  return HttpResponse(template.render(context))
