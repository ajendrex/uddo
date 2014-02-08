from django.shortcuts import get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.forms.models import inlineformset_factory
from django.forms.models import modelform_factory
from django.contrib.auth.models import User, Group

from recursos.models import Recurso, ComentarioRecurso, RecursoForm, InsumoRecurso
from cursos.models import Curso
from utils.userutils import *

@login_required
def index(request):
  u = request.user
  objetos = {}
  if usuarioEsCoordinador(u) or usuarioEsSupervisor(u):
    objetos["recursos_list"] = Recurso.objects.all()
  else:
    if usuarioEsProfesor(u):
      cursosProfesor = Curso.objects.filter(profesor=u)
      objetos["recursos_list"] = Recurso.objects.filter(curso__in=cursosProfesor)
    elif usuarioEsProveedor(u):
      objetos["recursos_list"] = Recurso.objects.filter(proveedor=u)
    elif usuarioEsDI(u):
      objetos["recursos_list"] = Recurso.objects.filter(creador=u)
    else:
      objetos["mensaje_de_error"] = "No posee privilegios para ver esta página"
      
  template = loader.get_template('recursos/index.html')
  context = RequestContext(request, objetos)
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
  comentario.save()
  return redirect(reverse('recursos:detalle', args=(c.id,)))

@login_required
def crearRecurso(request):
  objetos = {}
  if not usuarioEsDI(request.user):
    objetos["mensaje_de_error"] = "No posee privilegios para crear un recurso"
  else:
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
      objetos["recursoForm"] = RecursoForm()
      objetos["insumoFormset"] = InsumoFormset()

  template = loader.get_template('recursos/crearRecurso.html')
  context = RequestContext(request, objetos)
  return HttpResponse(template.render(context))

@login_required
def asignarProveedor(request, recurso_id):
  ProveedorForm = modelform_factory(Recurso, fields=('proveedor',))
  recurso = Recurso.objects.get(id=recurso_id)
  if request.method == 'POST':
    proveedorForm = ProveedorForm(request.POST, instance=recurso)
    recurso = proveedorForm.save()
    return redirect(reverse('recursos:detalle', args=(recurso.id,)))
  else:
    proveedorForm = ProveedorForm(instance=recurso)
    proveedorForm.fields["proveedor"].queryset = User.objects.filter(groups__name="Proveedores")

  template = loader.get_template('recursos/asignarProveedor.html')
  context = RequestContext(request, {'proveedorForm': proveedorForm, 'recurso': recurso})
  return HttpResponse(template.render(context))
