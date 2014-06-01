#encoding:utf-8
from bootstrap3_datetime.widgets import DateTimePicker
from django.forms import ModelForm

from django import forms

from models import Ficha, Requerimientos


class FichaForm(forms.ModelForm):
	class Meta:
		model 			= Ficha
		hora_programada = forms.DateTimeField(widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm",
                                       "pickSeconds": True}))

		exclude = ('km_inicio','km_termino','hora_inicio_Espera',
			'hora_llegada_Espera', 'hora_QTH_inicio', 'hora_QTH_final')
		


		

class EditarFichaForm(forms.ModelForm):
	class Meta:
		model = Ficha

class RequerimientosForm(forms.ModelForm):
	class Meta:
		model = Requerimientos 
	ficha = forms.CharField(widget=forms.HiddenInput())
