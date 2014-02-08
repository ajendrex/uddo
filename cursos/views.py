from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.views import generic
from cursos.models import Curso, ComentarioCurso
from django.contrib.auth.models import User

# Create your views here.
class IndexView(generic.ListView):
  template_name = 'cursos/index.html'
  context_object_name = 'latest_cursos_list'

  def get_queryset(self):
    """Retorna los últimos 5 cursos."""
    return Curso.objects.order_by('-fec_modificacion')[:5]

class DetailView(generic.DetailView):
  model = Curso
  template_name = 'cursos/detalle.html'

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
