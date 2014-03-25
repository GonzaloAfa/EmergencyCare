from django.contrib import admin
from ficha.models import Ficha 
from ficha.models import Sexo
from ficha.models import Causa
from ficha.models import TipoMovil
from ficha.models import EstadoFicha

# Register your models here.

admin.site.register(Sexo)
admin.site.register(Causa)
admin.site.register(TipoMovil)
admin.site.register(EstadoFicha)
admin.site.register(Ficha)

