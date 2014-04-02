from django.conf.urls import patterns, url

from modulos import views

urlpatterns = patterns('',
                       url(r'^(?P<curso_id>\d+)$', views.detalle, name='detalle'),
                       url(r'^(?P<curso_id>\d+)/crearModulo', views.crearModulo, name='crearModulo'),
                       )
