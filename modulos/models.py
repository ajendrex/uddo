from django.db import models
from cursos.models import Curso
from recursos.models import Recurso

class Modulo(models.Model):
  curso = models.ForeignKey(Curso, related_name="modulos")
  nombre_corto = models.CharField(max_length = 20)
  nombre_largo = models.CharField(max_length = 200)
  orden = models.IntegerField()

  def __str__(self):
    return self.curso.codigo + " - " + self.nombre_corto

class Imagen(models.Model):
  nombre = models.CharField(max_length = 20)
  archivo = models.FileField(upload_to="img/", max_length=255)

  def __str__(self):
    return self.nombre

class Pagina(models.Model):
  modulo = models.ForeignKey(Modulo, related_name="paginas")
  nombre_archivo = models.CharField(max_length = 30)
  titulo = models.CharField(max_length = 200)
  foto = models.ForeignKey(Imagen, related_name="paginas", null=True, blank=True)
  orden = models.IntegerField()

  def __str__(self):
    return str(self.modulo) + " - " + self.titulo

class Contenido(models.Model):
  pagina = models.ForeignKey(Pagina, related_name = "contenidos")
  orden = models.IntegerField()
  html = models.TextField()

class RecAprendizaje(models.Model):
  modulo = models.OneToOneField(Modulo, primary_key=True)
  categoria = models.CharField(max_length = 3,
                               choices = (('TAR', "Para realizar la Tarea"),
                                          ('OBL', "Obligatorios"),
                                          ('OPC', "Opcionales"),
                                          ('BIB', "Bibliografía"),
                                          ('MED', "Muldimedia")))
  recurso = models.ForeignKey(Recurso)
  leyenda = models.CharField(max_length = 300)
