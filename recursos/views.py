from django.shortcuts import get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.forms.models import inlineformset_factory
from django.forms.models import modelform_factory
from django.contrib.auth.models import User, Group
from django.contrib.admin import widgets
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from bootstrap3_datetime.widgets import DateTimePicker

from recursos.models import Recurso, ComentarioRecurso, InsumoRecurso, VersionRecurso
from recursos.forms import RecursoForm, VersionForm, ComentarioVersionRecurso
from cursos.models import Curso
from utils.utils import *
from utils.notificaciones import *

@login_required
def index(request):
  u = request.user
  objetos = {}
  columns = { 'nombre': "nombre",
              '-nombre': "-nombre",
              'curso': "curso",
              '-curso': "-curso",
              'creacion': "fecha_creacion",
              '-creacion': "-fecha_creacion",
              'proveedor': "proveedor",
              '-proveedor': "-proveedor",
              'entregaEstimada': "entrega_estimada",
              '-entregaEstimada': "-entrega_estimada",
            }
  sortby = request.GET.get('sortby')
  objetos["sortby"] = sortby
  if sortby in columns:
    sortString = columns[sortby]
  else:
    sortString = "?"

  if usuarioEsCoordinador(u) or usuarioEsSupervisor(u):
    recursos_list = Recurso.objects.all()
  else:
    if usuarioEsProfesor(u):
      cursosProfesor = Curso.objects.filter(profesor=u)
      recursos_list = Recurso.objects.filter(curso__in=cursosProfesor).order_by(sortString)
    elif usuarioEsProveedor(u):
      recursos_list = Recurso.objects.filter(proveedor=u).order_by(sortString)
    elif usuarioEsDI(u):
      recursos_list = Recurso.objects.filter(creador=u).order_by(sortString)
    else:
      objetos["mensaje_de_error"] = "No posee privilegios para ver esta página."
      template = loader.get_template('recursos/index.html')
      context = RequestContext(request, objetos)
      return HttpResponse(template.render(context))
  paginator = Paginator(recursos_list, 10)
  page = request.GET.get('page')
  try:
    objetos["recursos_list"] = paginator.page(page)
  except PageNotAnInteger:
    objetos["recursos_list"] = paginator.page(1)
  except EmptyPage:
    objetos["recursos_list"] = paginator.page(paginator.num_pages)
      
  template = loader.get_template('recursos/index.html')
  context = RequestContext(request, objetos)
  return HttpResponse(template.render(context))

@login_required
def detalle(request, recurso_id):
  objetos = {}
  recurso = Recurso.objects.get(id=recurso_id) 
  objetos["recurso"] = recurso
  u = request.user
  if usuarioEsProfesor(u):
    if recurso.curso.profesor != u:
      objetos["mensaje_de_error"] = "Usted no tiene privilegios para ver este recurso."
  elif usuarioEsProveedor(u):
    if recurso.proveedor != u:
      objetos["mensaje_de_error"] = "Usted no tiene privilegios para ver este recurso."
  elif not usuarioEsInterno(u):
    objetos["mensaje_de_error"] = "Usted no tiene privilegios para ver este recurso."

  template = loader.get_template('recursos/detalle.html')
  context = RequestContext(request, objetos)
  return HttpResponse(template.render(context))

@login_required
def comentar(request, recurso_id):
  recurso = get_object_or_404(Recurso, pk=recurso_id)

  comentario = ComentarioRecurso()
  comentario.autor = request.user
  comentario.recurso = recurso
  comentario.comentario = request.POST['texto']
  comentario.save()
  notificarComentarioRecurso(request, comentario)
  return redirect(reverse('recursos:detalle', args=(recurso.id,)))

@login_required
def crearRecurso(request):
  objetos = {}
  if not usuarioEsDI(request.user):
    objetos["mensaje_de_error"] = "Usted no posee privilegios para crear un recurso."
  else:
    InsumoFormset = inlineformset_factory(Recurso, InsumoRecurso, extra=1)
    if request.method == 'POST':
      recursoForm = RecursoForm(request.POST)
      insumoFormset = InsumoFormset(request.POST, request.FILES)
      if recursoForm.is_valid():
        recurso = recursoForm.save(commit=False)
        recurso.creador = request.user
        recurso.save()
        notificarCreacionRecurso(request, recurso)
        for insumoForm in insumoFormset:
          if insumoForm.is_valid() and not insumoForm.cleaned_data["DELETE"]:
            insumoRecurso = insumoForm.save(commit=False)
            if not insumoRecurso.archivo.name:
              continue
            insumoRecurso.recurso = recurso
            insumoRecurso.save()
        return redirect(reverse('recursos:detalle', args=(recurso.id,)))
      else:
        objetos["recursoForm"] = recursoForm
        objetos["insumoFormset"] = insumoFormset
    else:
      if "curso" in request.GET:
        objetos["recursoForm"] = RecursoForm(initial={'curso':int(request.GET["curso"])})
      else:
        objetos["recursoForm"] = RecursoForm()
      objetos["recursoForm"].fields["curso"].queryset = Curso.objects.filter(owner=request.user)
      objetos["insumoFormset"] = InsumoFormset()

  template = loader.get_template('recursos/crearRecurso.html')
  context = RequestContext(request, objetos)
  return HttpResponse(template.render(context))

@login_required
def editarRecurso(request, recurso_id):
  recurso = get_object_or_404(Recurso, pk=recurso_id)
  objetos = {}
  objetos["recurso"] = recurso
  u = request.user
  if recurso.creador != u and not (usuarioEsSupervisor(u) or usuarioEsCoordinador(u)):
      objetos["mensaje_de_error"] = "Usted no puede editar este recurso."
  else:
    InsumoFormset = inlineformset_factory(Recurso, InsumoRecurso, extra=1)
    if request.method == 'POST':
      recursoForm = RecursoForm(request.POST, instance=recurso)
      insumoFormset = InsumoFormset(request.POST, request.FILES, instance = recurso)
      if recursoForm.is_valid():
        recurso = recursoForm.save(commit=False)
        recurso.save()
        for insumoForm in insumoFormset:
          if insumoForm.is_valid():
            insumoRecurso = insumoForm.save(commit=False)
            if not insumoRecurso.archivo.name:
              continue
            insumoRecurso.save()
            if insumoForm.cleaned_data["DELETE"]:
              insumoRecurso.delete()
        return redirect(reverse('recursos:detalle', args=(recurso.id,)))
      else:
        objetos["recursoForm"] = recursoForm
        objetos["insumoFormset"] = insumoFormset
    else:
      objetos["recursoForm"] = RecursoForm(instance=recurso)
      objetos["recursoForm"].fields["curso"].queryset = Curso.objects.filter(owner=request.user)
      objetos["insumoFormset"] = InsumoFormset(instance=recurso)

  template = loader.get_template('recursos/editarRecurso.html')
  context = RequestContext(request, objetos)
  return HttpResponse(template.render(context))

@login_required
def asignarProveedor(request, recurso_id):
  ProveedorForm = modelform_factory(Recurso, fields=('proveedor',))
  recurso = Recurso.objects.get(id=recurso_id)
  proveedorAnterior = recurso.proveedor
  objetos = {"recurso": recurso}
  if not usuarioEsCoordinador(request.user):
    objetos["mensaje_de_error"] = "Usted no puede asignar proveedor al recurso."
  elif request.method == 'POST':
    proveedorForm = ProveedorForm(request.POST, instance=recurso)
    if proveedorForm.is_valid():
      r = proveedorForm.save(commit=False)
      if r.proveedor != proveedorAnterior:
        r.entrega_estimada = None
        notificarProveedorAsignado(request, r, proveedorAnterior)
      r.save()
      return redirect(reverse('recursos:detalle', args=(r.id,)))
    else:
      objetos["mensaje_de_error"] = "Algo salió mal..."
  else:
    objetos["proveedorForm"] = ProveedorForm(instance=recurso)
    objetos["proveedorForm"].fields["proveedor"].queryset = User.objects.filter(groups__name="Proveedores")

  template = loader.get_template('recursos/asignarProveedor.html')
  context = RequestContext(request, objetos)
  return HttpResponse(template.render(context))

@login_required
def definirFechaEntrega(request, recurso_id):
  EntregaForm = modelform_factory(Recurso,
                                  fields=('entrega_estimada',),
                                  widgets={'entrega_estimada':DateTimePicker(options={"format": "DD/MM/YYYY HH:mm",
                                                                         "pickSeconds": False})},)
  recurso = Recurso.objects.get(id=recurso_id)
  objetos = {"recurso": recurso}
  if recurso.entrega_estimada:
    objetos["mensaje_de_error"] = "No puede modificar la fecha ya informada."
  elif recurso.proveedor != request.user:
    objetos["mensaje_de_error"] = "Usted no ha sido asignado para producir este recurso."
  else:
    if request.method == 'POST':
      entregaForm = EntregaForm(request.POST, instance=recurso)
      if entregaForm.is_valid():
        entregaForm.save()
        notificarAsignacionAceptada(request, recurso)
        return redirect(reverse('recursos:detalle', args=(recurso.id,)))
      else:
        objetos["mensaje_de_error"] = "Fecha ingresada no es válida."
    else:
      objetos["entregaForm"] = EntregaForm(instance=recurso)

  template = loader.get_template('recursos/definirFechaEntrega.html')
  context = RequestContext(request, objetos)
  return HttpResponse(template.render(context))

@login_required
def entregar(request, recurso_id):
  recurso = Recurso.objects.get(id=recurso_id)
  objetos = {}
  if recurso.proveedor != request.user:
    objetos["mensaje_de_error"] = "Usted no puede entregar una versión para este recurso."
  else:
    if request.method == 'POST':
      versionForm = VersionForm(request.POST, request.FILES)
      if versionForm.is_valid():
        version = versionForm.save(commit=False)
        version.recurso_id = recurso.id
        version.version = recurso.total_versiones + 1
        version.proveedor = request.user
        version.save()
        recurso.total_versiones += 1
        recurso.save()
        notificarEntrega(request, version)
        return redirect(reverse('recursos:detalle', args=(recurso.id,)))
      else:
        objetos["mensaje_de_error"] = "Hubo un error subiendo el archivo."
    else:
      objetos["recurso"] = recurso
      objetos["versionForm"] = VersionForm(instance=recurso)

  template = loader.get_template('recursos/entregar.html')
  context = RequestContext(request, objetos)
  return HttpResponse(template.render(context))

@login_required
def detalleVersionRecurso(request, version_id):
  objetos = {}
  version = VersionRecurso.objects.get(id=version_id) 
  objetos["version"] = version
  objetos["mostrarBotonAprobacion"] = False
  u = request.user
  if usuarioEsProfesor(u):
    if version.recurso.curso.profesor != u:
      objetos["mensaje_de_error"] = "Usted no tiene privilegios para ver este recurso."
    if not version.aprobado_profesor:
      objetos["mostrarBotonAprobacion"] = True
  elif usuarioEsProveedor(u):
    if version.recurso.proveedor != u:
      objetos["mensaje_de_error"] = "Usted no tiene privilegios para ver este recurso."
  elif usuarioEsDI(u):
    if not version.aprobado_di:
      objetos["mostrarBotonAprobacion"] = True
  elif usuarioEsCoordinador(u):
    if not version.aprobado_coordinador:
      objetos["mostrarBotonAprobacion"] = True
  elif not usuarioEsInterno(u):
    objetos["mensaje_de_error"] = "Usted no tiene privilegios para ver este recurso."

  template = loader.get_template('recursos/detalleVersionRecurso.html')
  context = RequestContext(request, objetos)
  return HttpResponse(template.render(context))

@login_required
def comentarVersion(request, version_id):
  v = get_object_or_404(VersionRecurso, pk=version_id)

  comentario = ComentarioVersionRecurso()
  comentario.autor = request.user
  comentario.version = v
  comentario.comentario = request.POST['texto']
  comentario.save()
  notificarComentarioVersion(request, comentario)
  return redirect(reverse('recursos:detalleVersionRecurso', args=(v.id,)))

@login_required
def aprobarVersion(request, version_id):
  v = get_object_or_404(VersionRecurso, pk=version_id)
  u = request.user

  if usuarioEsDI(u) and v.recurso.creador == u:
    v.aprobado_di = True
  if usuarioEsProfesor(u) and v.recurso.curso.profesor == u:
    v.aprobado_profesor = True
  if usuarioEsCoordinador(u):
    v.aprobado_coordinador = True

  v.save()
  return redirect(reverse('recursos:detalleVersionRecurso', args=(v.id,)))
