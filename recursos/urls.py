from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from recursos import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^crearRecurso/$', views.crearRecurso, name="crearRecurso"),
                       url(r'^(?P<recurso_id>\d+)/$', views.detalle, name="detalle"),
                       url(r'^(?P<recurso_id>\d+)/comentar/$', views.comentar, name="comentar"),
                       url(r'^(?P<recurso_id>\d+)/asignarProveedor/$', views.asignarProveedor, name="asignarProveedor"),
                       url(r'^(?P<recurso_id>\d+)/definirFechaEntrega/$', views.definirFechaEntrega, name="definirFechaEntrega"),
                       )
