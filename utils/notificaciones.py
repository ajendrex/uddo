from django.core.mail import send_mail
from django.contrib.auth.models import User
from utils.utils import *
from pprint import *

remitente = 'notificaciones-uddo@unab.cl'

def notificarCreacionCurso(request, curso):
  asuntoCursoCreado = "Curso Creado en Unidad de Diseño y Desarrollo Online"
  di = curso.owner
  profesor = curso.profesor
  cursoReferencia = str(curso) + " (" + getCursoUrl(request, curso) + ")"
  msg = "Hola " + di.get_full_name() + ",\n\nel curso " + cursoReferencia + " ha sido creado exitosamente.\n\nSaludos atentos."
  send_mail(asuntoCursoCreado, msg, remitente, [di.email], fail_silently=True)
  msg = "Estimado(a) profesor(a) " + profesor.get_full_name() + ",\n\nle informamos que el curso " + cursoReferencia + " ha sido creado en el sistema de información de la Unidad de Diseño y Desarrollo Online. Usted ha sido definido como el profesor de este curso.\n\nSi no tiene credenciales para entrar a ver el curso (y eventualmente los recursos de aprendizaje asociados) por favor comuníquese con " + di.get_full_name() + ", al email " + di.email + ".\n\nSaludos atentos."
  send_mail(asuntoCursoCreado, msg, remitente, [profesor.email], fail_silently=True)

def notificarCreacionRecurso(request, recurso):
  asuntoRecursoCreado = "Recurso Creado en Unidad de Diseño y Desarrollo Online"
  di = recurso.creador
  recursoReferencia = str(recurso) + " (" + getRecursoUrl(request, recurso) + ")"
  msg = "Hola " + di.get_full_name() + ",\n\nel recurso " + recursoReferencia + " ha sido creado exitosamente.\n\nSaludos atentos."
  send_mail(asuntoRecursoCreado, msg, remitente, [di.email], fail_silently=True)

def notificarProveedorAsignado(request, recurso, proveedorAnterior):
  asuntoProveedorAsignado = "Proveedor Asignado en Unidad de Diseño y Desarrollo Online"
  di = recurso.creador
  proveedor = recurso.proveedor
  recursoReferencia = str(recurso) + " (" + getRecursoUrl(request, recurso) + ")"
  if proveedorAnterior:
    msg = "Hola " + proveedorAnterior.get_full_name() + ",\n\nle informamos que, de acuerdo a nuestros registros, usted ya no debe producir el recurso de aprendizaje " + recursoReferencia + ". Esto puede deberse a distintas razones; si usted no sabe cuál es, puede contactarse el coordinador de recursos de la Unidad de Diseño y Desarrollo Online y saber más detalles.\n\nSaludos atentos."
    send_mail(asuntoProveedorAsignado, msg, remitente, [proveedorAnterior.email], fail_silently=True)
    msg = "Hola " + di.get_full_name() + ",\n\nte informamos que el proveedor " + proveedorAnterior.get_full_name() + " ya no debe producir el recurso de aprendizaje " + recursoReferencia + ".\n\nSaludos atentos."
    send_mail(asuntoProveedorAsignado, msg, remitente, [di.email], fail_silently=True)
  if proveedor:
    msg = "Hola " + proveedor.get_full_name() + ",\n\nle informamos que usted ha sido asignado(a) para producir el recurso de aprendizaje " + recursoReferencia + ". Para aceptar la asignación, por favor entre a la plataforma e informe una fecha de entrega estimada.\n\nSaludos atentos."
    send_mail(asuntoProveedorAsignado, msg, remitente, [proveedor.email], fail_silently=True)
    msg = "Hola " + di.get_full_name() + ",\n\nte informamos que el proveedor " + proveedor.get_full_name() + " ha sido asignado para producir el recurso de aprendizaje " + recursoReferencia + ".\n\nSaludos atentos."
    send_mail(asuntoProveedorAsignado, msg, remitente, [di.email], fail_silently=True)

def notificarAsignacionAceptada(request, recurso):
  asunto = "Proveedor acepta asignación de recurso en Unidad de Diseño y Desarrollo Online"
  di = recurso.creador
  proveedor = recurso.proveedor
  recursoReferencia = str(recurso) + " (" + getRecursoUrl(request, recurso) + ")"
  msg = "Hola " + di.get_full_name() + ",\n\nte informamos que el proveedor " + proveedor.get_full_name() + " aceptó la producción del recurso de aprendizaje " + recursoReferencia + ", definiendo como fecha de entrega estimada " + str(recurso.entrega_estimada) + ".\n\nSaludos atentos."
  send_mail(asunto, msg, remitente, [di.email], fail_silently=True)

def notificarEntrega(request, version):
  asunto = "Proveedor entrega nueva versión de recurso en Unidad de Diseño y Desarrollo Online"
  di = version.recurso.creador
  proveedor = version.proveedor
  recursoReferencia = str(version.recurso) + " versión " + str(version.version) + " (" + getVersionUrl(request, version) + ")"
  msg = "Hola " + di.get_full_name() + ",\n\nte informamos que el proveedor " + proveedor.get_full_name() + " entregó el siguiente recurso: " + recursoReferencia + ".\n\nSaludos atentos."
  send_mail(asunto, msg, remitente, [di.email], fail_silently=True)

def notificarComentarioRecurso(request, comentario):
  nombreAutor = comentario.autor.get_full_name()
  asunto = nombreAutor + " comentó un recurso en Unidad de Diseño y Desarrollo Online"
  recursoReferencia = str(comentario.recurso) + " (" + getRecursoUrl(request, comentario.recurso) + ")"
  participantes = comentario.recurso.getComentaristas()
  for p in participantes:
    if p != comentario.autor:
      msg = "Hola " + p.get_full_name() + ",\n\n" + nombreAutor + " ha hecho un comentario para el recurso " + recursoReferencia + ".\n\n El comentario ingresado fué:\n\n\"" + comentario.comentario + "\".\n\nSaludos atentos."
      send_mail(asunto, msg, remitente, [p.email], fail_silently=True)

def notificarComentarioVersion(request, comentario):
  nombreAutor = comentario.autor.get_full_name()
  asunto = nombreAutor + " comentó la entrega de un recurso en Unidad de Diseño y Desarrollo Online"
  recursoReferencia = str(comentario.version.recurso) + " versión " + str(comentario.version.version) + " (" + getVersionUrl(request, comentario.version) + ")"
  participantes = comentario.version.getComentaristas()
  for p in participantes:
    if p != comentario.autor:
      msg = "Hola " + p.get_full_name() + ",\n\n" + nombreAutor + " ha hecho un comentario para la entrega " + recursoReferencia + ".\n\n El comentario ingresado fué:\n\n\"" + comentario.comentario + "\".\n\nSaludos atentos."
      send_mail(asunto, msg, remitente, [p.email], fail_silently=True)
