from django.conf.urls import patterns, url

from cursos import views

urlpatterns = patterns('',
                       url(r'^$', views.IndexView.as_view(), name='index'),
                       url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name="detalle"),
                       url(r'^(?P<curso_id>\d+)/comentar/$', views.comentar, name="comentar"),
                       )
