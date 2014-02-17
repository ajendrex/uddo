from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'uddo.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cursos/', include('cursos.urls', namespace='cursos')),
    url(r'^recursos/', include('recursos.urls', namespace='recursos')),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
