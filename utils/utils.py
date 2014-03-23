from django.contrib.auth.models import User, Group
import sys
from django.core.urlresolvers import reverse
from cursos.models import Curso
from django.http import HttpRequest

def usuarioEsSupervisor(u):
  supervisoresGroup, created = Group.objects.get_or_create(name="Supervisores")
  return supervisoresGroup in u.groups.all()

def usuarioEsCoordinador(u):
  coordinadoresGroup, created = Group.objects.get_or_create(name="Coordinadores")
  return coordinadoresGroup in u.groups.all()

def usuarioEsProfesor(u):
  profesoresGroup, created = Group.objects.get_or_create(name="Profesores")
  return profesoresGroup in u.groups.all()

def usuarioEsProveedor(u):
  proveedoresGroup, created = Group.objects.get_or_create(name="Proveedores")
  return proveedoresGroup in u.groups.all()

def usuarioEsDI(u):
  diGroup, created = Group.objects.get_or_create(name="DI")
  return diGroup in u.groups.all()

def usuarioEsInterno(u):
  return usuarioEsSupervisor(u) or usuarioEsCoordinador(u) or usuarioEsDI(u)

def getCursoUrl(request, curso):
  return request.build_absolute_uri(reverse('cursos:detalle', args=(curso.id,)))

def getRecursoUrl(request, recurso):
  return request.build_absolute_uri(reverse('recursos:detalle', args=(recurso.id,)))

def getVersionUrl(request, version):
  return request.build_absolute_uri(reverse('recursos:detalleVersionRecurso', args=(version.id,)))
