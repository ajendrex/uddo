# -*- coding: utf-8 -*-

from django.forms import ModelForm
from modulos.models import *

class ModuloForm(ModelForm):
  class Meta:
    model = Modulo
    fields = ['nombre_corto', 'nombre_largo']

class PaginaForm(ModelForm):
  class Meta:
    model = Pagina
    fields = ['nombre_archivo', 'titulo', 'foto', 'orden'] 
