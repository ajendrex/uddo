from django.contrib.auth.models import User, Group
import sys

try:
  supervisoresGroup = Group.objects.get(name="Supervisores")
  coordinadoresGroup = Group.objects.get(name="Coordinadores")
  profesoresGroup = Group.objects.get(name="Profesores")
  proveedoresGroup = Group.objects.get(name="Proveedores")
  diGroup = Group.objects.get(name="DI")
except Exception:
  print("Error, debe comentar creación de objetos en utils.py y crear los grupos en base de datos. Luego descomentar las líneas comentadas", out=sys.stderr)

def usuarioEsSupervisor(u):
  return supervisoresGroup in u.groups.all()

def usuarioEsCoordinador(u):
  return coordinadoresGroup in u.groups.all()

def usuarioEsProfesor(u):
  return profesoresGroup in u.groups.all()

def usuarioEsProveedor(u):
  return proveedoresGroup in u.groups.all()

def usuarioEsDI(u):
  return diGroup in u.groups.all()

def usuarioEsInterno(u):
  return usuarioEsSupervisor(u) or usuarioEsCoordinador(u) or usuarioEsDI(u)
