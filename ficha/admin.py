from django.contrib import admin
from ficha.models import Ficha, Movil, Servicio, Traslado

# Register your models here.

admin.site.register(Ficha)
admin.site.register(Movil)
admin.site.register(Servicio)
admin.site.register(Traslado)

