# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User, Group
from cursos.models import Curso
from utils.utils import *
import datetime
import os


# Create your models here.
class Recurso(models.Model):
  nombre = models.CharField(max_length = 100)
  curso = models.ForeignKey(Curso, null=True, related_name="recursos")
  creador = models.ForeignKey(User, related_name = "recursos_di")
  tipo = models.CharField(max_length = 3,
                          choices = (('INT', "Interactivo"),
                                     ('REC', "Recreación"),
                                     ('ANI', "Animación"),
                                     ('ENT', "Entrevista"),
                                     ('DIG', "Digitalización"),
                                     ('DIA', "Diagramación"),
                                     ('GRA', "Gráfica"),
                                     ('FOT', "Fotografía"),
                                     ('EST', "Estilaje")))
  categoria = models.CharField(max_length = 1,
                               choices = (('B', "Básico"),
                                          ('M', "Medio"),
                                          ('F', "Full"),
                                          ('E', "Especial")))
  proveedor = models.ForeignKey(User, null = True, blank=True, related_name = "recursos_prov")
  costo = models.IntegerField(null=True, blank=True)
  costoFinal = models.IntegerField(null=True, blank=True)
  descripcion = models.TextField(blank=True)
  link = models.CharField(max_length = 300, blank=True)
  fecha_creacion = models.DateTimeField(auto_now_add = True)
  entrega_estimada = models.DateTimeField(null=True, blank=True)
  total_versiones = models.IntegerField(default=0)

  def __str__(self):
    return self.nombre

  def cantEntregas(self):
    return self.versiones.count()

  def sinEntregas(self):
    return not self.cantEntregas()

  def ultimaEntrega(self):
    if self.cantEntregas():
      return self.versiones.all()[self.cantEntregas() - 1]
    return None

  def entregaAtrasada(self):
    if self.sinEntregas():
      return True
    return self.entrega_estimada <= self.ultimaEntrega().fecha_entrega

  def getComentaristas(self):
    comentaristas = [self.creador]
    if self.proveedor:
      comentaristas.append(self.proveedor)
    for comentario in self.comentarios.all():
      if (usuarioEsSupervisor(comentario.autor) or usuarioEsCoordinador(comentario.autor)) and comentario.autor not in comentaristas:
        comentaristas.append(comentario.autor)
    return comentaristas

class InsumoRecurso(models.Model):
  archivo = models.FileField(upload_to="insumos/%Y/%m/%d/", max_length=255)
  recurso = models.ForeignKey(Recurso, related_name="insumos")

  def __str__(self):
    return os.path.basename(self.archivo.name)

class VersionRecurso(models.Model):
  archivo = models.FileField(upload_to="versiones/%Y/%m/%d/", max_length=255)
  fecha_entrega = models.DateTimeField(auto_now_add = True)
  recurso = models.ForeignKey(Recurso, related_name="versiones")
  version = models.IntegerField()
  proveedor = models.ForeignKey(User, related_name="entregas")
  aprobado_di = models.BooleanField(default=False)
  aprobado_profesor = models.BooleanField(default=False)
  aprobado_coordinador = models.BooleanField(default=False)

  def __str__(self):
    return os.path.basename(self.archivo.name)

  def aprobado(self):
    return self.aprobado_di and self.aprobado_profesor and self.aprobado_coordinador
  
  def getComentaristas(self):
    comentaristas = [self.recurso.creador, self.proveedor]
    for comentario in self.comentarios.all():
      if (usuarioEsSupervisor(comentario.autor) or usuarioEsCoordinador(comentario.autor)) and comentario.autor not in comentaristas:
        comentaristas.append(comentario.autor)
    return comentaristas

class Tag(models.Model):
  tag = models.CharField(max_length = 100, unique=True)
  recursos = models.ManyToManyField(Recurso, related_name="tags")

class ComentarioRecurso(models.Model):
  autor = models.ForeignKey(User, null=True, related_name="comentariosEnRecursos")
  recurso = models.ForeignKey(Recurso, related_name="comentarios")
  comentario = models.TextField()
  fec_creacion = models.DateTimeField(auto_now_add = True)

  def autorEsProveedor(self):
    return usuarioEsProveedor(self.autor)

class ComentarioVersionRecurso(models.Model):
  autor = models.ForeignKey(User, null=True, related_name="comentariosEnEntregas")
  version = models.ForeignKey(VersionRecurso, related_name="comentarios")
  comentario = models.TextField()
  fec_creacion = models.DateTimeField(auto_now_add = True)

  def autorEsProveedor(self):
    return usuarioEsProveedor(self.autor)
