from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$','ficha.views.index'),
    url(r'^login/$', 'ficha.views.user_login', name ='login'),
 #   url(r'^login/$','ficha.views.ingresar'),
    url(r'^logout/$','ficha.views.cerrar', name ='logout'),
    
    url(r'^home/$','ficha.views.ficha_redirect', name ='home'),
    url(r'^ficha/ingresar$','ficha.views.ficha_ingresar', name='ingresar'),



    url(r'^ficha/ver/(?P<folio>\d+)$','ficha.views.ficha_ver', name='ver'),
    url(r'^ficha/modificar/(?P<folio>\d+)$','ficha.views.ficha_modificar', name='modificar'),

    url(r'^ficha/evaluador/(?P<ficha>\d+)$','ficha.views.complejidad', name ='evaluador'),
    

    url(r'^listado/$','ficha.views.ficha_redirect', name='listado_fichas'),
    url(r'^listado/(?P<page>\d+)$','ficha.views.ficha_listado', name='listado'),

    url(r'^archivados/$','ficha.views.ficha_archivados_redirect', name='fichas_archivadas'),
    url(r'^archivados/(?P<page>\d+)$','ficha.views.ficha_archivados', name='archivados'),
  

   	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
	
	url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
	)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
