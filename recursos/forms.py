# -*- coding: utf-8 -*-

from django.forms import ModelForm
from recursos.models import *
#from django.contrib.auth.models import User

class RecursoForm(ModelForm):
  class Meta:
    model = Recurso
    fields = ['nombre', 'curso', 'tipo', 'categoria', 'descripcion']

class VersionForm(ModelForm):
  class Meta:
    model = VersionRecurso
    fields = ['archivo']
