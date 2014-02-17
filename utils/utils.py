from django.contrib.auth.models import User, Group
import sys

def usuarioEsSupervisor(u):
  supervisoresGroup = Group.objects.get(name="Supervisores")
  return supervisoresGroup in u.groups.all()

def usuarioEsCoordinador(u):
  coordinadoresGroup = Group.objects.get(name="Coordinadores")
  return coordinadoresGroup in u.groups.all()

def usuarioEsProfesor(u):
  profesoresGroup = Group.objects.get(name="Profesores")
  return profesoresGroup in u.groups.all()

def usuarioEsProveedor(u):
  proveedoresGroup = Group.objects.get(name="Proveedores")
  return proveedoresGroup in u.groups.all()

def usuarioEsDI(u):
  diGroup = Group.objects.get(name="DI")
  return diGroup in u.groups.all()

def usuarioEsInterno(u):
  return usuarioEsSupervisor(u) or usuarioEsCoordinador(u) or usuarioEsDI(u)
