# -*- coding: utf-8 -*-

from django.forms import ModelForm
from cursos.models import *
#from django.contrib.auth.models import User

class CursoForm(ModelForm):
  class Meta:
    model = Curso
    fields = ['codigo', 'nombre', 'profesor']

  def __init__(self,*args,**kwargs):
    super (CursoForm,self ).__init__(*args,**kwargs)
    self.fields['profesor'].queryset = User.objects.filter(groups__name="Profesores")
