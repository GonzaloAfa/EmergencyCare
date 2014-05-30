from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$','ficha.views.index'),
    url(r'^login/$', 'ficha.views.user_login'),
 #   url(r'^login/$','ficha.views.ingresar'),
    url(r'^logout/$','ficha.views.cerrar'),
    
    url(r'^home/$','ficha.views.ficha_redirect'),
    url(r'^ficha/$','ficha.views.ficha_ingresar'),

    url(r'^complejidad/$','ficha.views.complejidad'),


    url(r'^ficha/(?P<folio>\d+)$','ficha.views.ficha_ver'),
    url(r'^ficha/modificar/(?P<folio>\d+)$','ficha.views.ficha_modificar'),
    
    url(r'^ficha/listado/$','ficha.views.ficha_redirect'),
    url(r'^ficha/listado/(?P<page>\d+)$','ficha.views.ficha_listado'),

    url(r'^archivados/$','ficha.views.ficha_archivados_redirect'),
    url(r'^ficha/archivados/(?P<page>\d+)$','ficha.views.ficha_archivados'),
  

   	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
	
	url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
	)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
