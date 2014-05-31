#encoding:utf-8
from bootstrap3_datetime.widgets import DateTimePicker

from django import forms
from models import Ficha, Requerimientos


class FichaForm(forms.ModelForm):
	class Meta:
		model = Ficha
		exclude = ('km_inicio','km_termino','hora_inicio_Espera',
			'hora_llegada_Espera', 'hora_QTH_inicio', 'hora_QTH_final')

		hora_programada = forms.DateTimeField(
			required=False,
			widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm",
				"pickSeconds": False}))

class EditarFichaForm(forms.ModelForm):
	class Meta:
		model = Ficha

class RequerimientosForm(forms.ModelForm):
	class Meta:
		model = Requerimientos 
	ficha = forms.CharField(widget=forms.HiddenInput())
