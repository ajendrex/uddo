from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template import RequestContext, loader
from django.http import HttpResponse

from cursos.models import Curso, ComentarioCurso
from cursos.forms import CursoForm
from utils.utils import *

# Create your views here.
class IndexView(generic.ListView):
  model = Curso
  template_name = 'cursos/index.html'
  context_object_name = 'latest_cursos_list'

@login_required
def index(request):
  u = request.user
  objetos = {}
  if usuarioEsCoordinador(u) or usuarioEsSupervisor(u):
    objetos["cursos_list"] = Curso.objects.all()
  else:
    if usuarioEsProfesor(u):
      objetos["cursos_list"] = Curso.objects.filter(profesor=u)
    elif usuarioEsDI(u):
      objetos["cursos_list"] = Curso.objects.filter(owner=u)
    else:
      objetos["mensaje_de_error"] = "No posee privilegios para ver esta página."
      
  template = loader.get_template('cursos/index.html')
  context = RequestContext(request, objetos)
  return HttpResponse(template.render(context))


class DetailView(generic.DetailView):
  model = Curso
  template_name = 'cursos/detalle.html'

@login_required
def comentar(request, curso_id):
  c = get_object_or_404(Curso, pk=curso_id)

  if not request.user.is_authenticated():
    return redirect('/login/?next=%s' % reverse('cursos:detalle', args=(c.id,)))

  comentario = ComentarioCurso()
  comentario.owner = request.user
  comentario.curso = c
  comentario.estado = 'NI'
  comentario.comentario = request.POST['texto']
  comentario.save()
  return redirect(reverse('cursos:detalle', args=(c.id,)))

@login_required
def crearCurso(request):
  objetos = {}
  if not usuarioEsDI(request.user):
    objetos["mensaje_de_error"] = "Usted no posee privilegios para crear un curso."
  else:
    if request.method == 'POST':
      cursoForm = CursoForm(request.POST)
      if cursoForm.is_valid():
        curso = cursoForm.save(commit=False)
        curso.owner = request.user
        curso.save()
        return redirect(reverse('cursos:detalle', args=(curso.id,)))
      else:
        objetos["mensaje_de_error"] = "Los datos ingresados no son correctos!."
        objetos["errores"] = cursoForm.errors
    else:
      objetos["cursoForm"] = CursoForm()

  template = loader.get_template('cursos/crearCurso.html')
  context = RequestContext(request, objetos)
  return HttpResponse(template.render(context))
