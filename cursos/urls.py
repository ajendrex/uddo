from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from cursos import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'crearCurso', views.crearCurso, name='crearCurso'),
                       url(r'^(?P<curso_id>\d+)/$', views.detalle, name="detalle"),
                       url(r'^(?P<curso_id>\d+)/comentar/$', views.comentar, name="comentar"),
                       )
