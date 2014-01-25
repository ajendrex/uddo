# -*- coding: latin-1 -*-

from django.db import models
from django.contrib.auth.models import User
from cursos.models import Curso

# Create your models here.
class Recurso(models.Model):
  nombre = models.CharField(max_length = 100)
  curso = models.ForeignKey(Curso, null=True)
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
  descripcion = models.CharField(max_length = 5000, blank=True)
  link = models.CharField(max_length = 300, blank=True)

  def __str__(self):
    return self.nombre

class InsumoRecurso(models.Model):
  archivo = models.FileField(upload_to="insumos/%Y/%m/%d/")
  recurso = models.ForeignKey(Recurso)

class VersionRecurso(models.Model):
  archivo = models.FileField(upload_to="versiones/%Y/%m/%d/")
  recurso = models.ForeignKey(Recurso)

class Tag(models.Model):
  tag = models.CharField(max_length = 100, unique=True)
  recursos = models.ManyToManyField(Recurso, related_name="tags")

class FechaEntrega(models.Model):
  fecha = models.DateTimeField()
  recurso = models.ForeignKey(Recurso)

class ComentarioRecurso(models.Model):
  owner = models.ForeignKey(User)
  recurso = models.ForeignKey(Recurso)
  comentario = models.TextField()
  fec_comentario = models.DateTimeField() #La fecha del comentario será de libre definición por el comentado
  fec_creacion = models.DateTimeField(auto_now_add = True) #Esta fecha será la real en que se crea el comentario
