#encoding:utf-8
from bootstrap3_datetime.widgets import DateTimePicker
from django.forms import ModelForm

from django import forms

from models import *


class FichaForm(forms.ModelForm):
	class Meta:
		model 	= Ficha		

		
class EditarFichaForm(forms.ModelForm):
	class Meta:
		model 	= Ficha

class EditarTraslado(forms.ModelForm):
	class Meta:
		model 	= Traslado
