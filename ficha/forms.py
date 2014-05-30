from django import forms
from models import Ficha, Requerimientos


class FichaForm(forms.ModelForm):
	class Meta:
		model = Ficha
		exclude = ('hora_inicio','hora_llegada','hora_QTH_inicio','hora_QTH_final')

class EditarFichaForm(forms.ModelForm):
	class Meta:
		model = Ficha

class RequerimientosForm(forms.ModelForm):
	class Meta:
		model = Requerimientos 

class IngresarFichaForm(forms.Form):

#	estado_ficha   	= forms.ForeignKey(EstadoFicha)

	
	nombre			= forms.CharField(max_length=60)
	apellido 		= forms.CharField(max_length=60)
	rut				= forms.CharField(max_length=12)
	edad			= forms.IntegerField()
#	sexo 			= forms.ForeignKey(Sexo)
	diagnostico		= forms.CharField()


	#Datos del traslado
	responsable 	= forms.CharField(max_length=60)
	telefono		= forms.CharField(max_length=13)
	origen			= forms.CharField(max_length=120)
	medico_derivador= forms.CharField(max_length=60)
	destino			= forms.CharField(max_length=120)
	medico_receptor	= forms.CharField(max_length=60)
#	causa			= forms.ForeignKey(Causa)


	#Datos gravedad del paciente
#	tipo_movil 		= forms.ForeignKey(TipoMovil)

	#datos internos que despues se modifican
	km_inicio		= forms.IntegerField(help_text="Ingrese en formano 24 hrs. Ejemplo 22:00")
	km_termino		= forms.IntegerField(help_text="Ingrese en formano 24 hrs. Ejemplo 22:00")
	hora_inicio		= forms.CharField(max_length=5, help_text="Ingrese en formano 24 hrs. Ejemplo 22:00")
	hora_llegada	= forms.CharField(max_length=5, help_text="Ingrese en formano 24 hrs. Ejemplo 22:00")
	
	hora_QTH_inicio	= forms.CharField(max_length=5, help_text="Ingrese en formano 24 hrs. Ejemplo 22:00")
	hora_QTH_final	= forms.CharField(max_length=5, help_text="Ingrese en formano 24 hrs. Ejemplo 22:00")


#class LoginForm(forms.Form):
#	username		= forms.CharField(max_length=60)
#	password		= forms.CharField(max_length=60)

