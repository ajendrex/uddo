from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from recursos import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^crearRecurso/$', views.crearRecurso, name="crearRecurso"),
                       url(r'^(?P<recurso_id>\d+)/$', views.detalle, name="detalle"),
                       url(r'^(?P<recurso_id>\d+)/editarRecurso/$', views.editarRecurso, name="editarRecurso"),
                       url(r'^(?P<recurso_id>\d+)/comentar/$', views.comentar, name="comentar"),
                       url(r'^(?P<recurso_id>\d+)/asignarProveedor/$', views.asignarProveedor, name="asignarProveedor"),
                       url(r'^(?P<recurso_id>\d+)/definirFechaEntrega/$', views.definirFechaEntrega, name="definirFechaEntrega"),
                       url(r'^(?P<recurso_id>\d+)/entregar/$', views.entregar, name="entregar"),
                       url(r'^entregas/(?P<version_id>\d+)/$', views.detalleVersionRecurso, name="detalleVersionRecurso"),
                       url(r'^entregas/(?P<version_id>\d+)/comentarVersion/$', views.comentarVersion, name="comentarVersion"),
                       url(r'^entregas/(?P<version_id>\d+)/aprobar/$', views.aprobarVersion, name="aprobarVersion"),
                       )
