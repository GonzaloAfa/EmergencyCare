from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$','ficha.views.index'),
    url(r'^home/$','ficha.views.enlista', name ='home'),

    url(r'^login/$', 'sesion.views.user_login', name ='login'),
    url(r'^logout/$','sesion.views.cerrar' , name ='logout'),
    

   url(r'^listado/$','ficha.views.enlista', name='enlista'),

#Fichas
    url(r'^derivacion/ingresar$','ficha.views.ficha_ingresar', name='ingresar_ficha'),
    url(r'^derivacion/ver/(?P<folio>\d+)$','ficha.views.ficha_ver', name='ver_ficha'),
    url(r'^derivacion/editar/(?P<folio>\d+)$','ficha.views.ficha_editar', name='editar_ficha'),

    url(r'^derivacion/traslado/(?P<folio>\d+)$','ficha.views.traslado_agregar', name='traslado_agregar'),

   url(r'^evaluar/$','diagnostico.views.evaluador', name='evaluador'),
   url(r'^diagnostico/$','diagnostico.views.diagnostico', name='diagnostico'),

#    url(r'^ficha/evaluador/(?P<ficha>\d+)$','ficha.views.complejidad', name ='evaluador'),
    

#    url(r'^listado/(?P<page>\d+)$','ficha.views.ficha_listado', name='listado'),

#    url(r'^archivados/$','ficha.views.ficha_archivados_redirect', name='fichas_archivadas'),
#    url(r'^archivados/(?P<page>\d+)$','ficha.views.ficha_archivados', name='archivados'),
  

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    )+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
