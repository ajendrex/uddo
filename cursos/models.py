# -*- coding: latin-1 -*-

from django.db import models
from django.contrib.auth.models import User

class Curso(models.Model):
  owner = models.ForeignKey(User, related_name = "cursos_di")
  profesor = models.ForeignKey(User, null = True, related_name = "cursos_prof")
  codigo = models.CharField(max_length = 20)
  nombre = models.CharField(max_length = 200)
  fec_creacion = models.DateTimeField(auto_now_add = True)
  fec_modificacion = models.DateTimeField(auto_now = True)

  def __str__(self):
    return self.codigo

class ComentarioCurso(models.Model):
  owner = models.ForeignKey(User)
  curso = models.ForeignKey(Curso)
  estado = models.CharField(max_length = 2,
                            choices = (('NI', 'No Iniciado'),
                                       ('DC', 'Diseño Conceptual'),
                                       ('DT', 'Diseño Detallado'),
                                       ('DR', 'Diseño de Recursos'),
                                       ('IM', 'Implantación'),
                                       ('RV', 'Revisión'),
                                       ('EN', 'Entregado')))
  comentario = models.TextField()
  fec_creacion = models.DateTimeField(auto_now_add = True) #Esta fecha será la real en que se crea el comentario

  def __str__(self):
    return "comentario de " + str(self.owner) + " en " + str(self.curso)

class Modulo(models.Model):
  curso = models.ForeignKey(Curso)
  orden = models.IntegerField()
  titulo = models.CharField(max_length = 200)
  nombreCorto = models.CharField(max_length = 20)

  def __str__(self):
    return self.nombreCorto
