from django.conf.urls import patterns, url

from recursos import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name="detalle"),
                       url(r'^(?P<recurso_id>\d+)/comentar/$', views.comentar, name="comentar"),
                       )
