from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

#autentificacion
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required


#usar name url para redireccionar
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
import json

from diagnostico.models import CHOICES_OXIGENOTERAPIA, CHOICES_ACCESO, CHOICES_HEMODINAMIA, CHOICES_VENTILATORIO, CHOICES_GLASGOW

def diagnostico(request):

	data 			= {}
	data['value'] 	= 0

	if request.POST:

		# Boolean
		monitorizacion 			= u'2' if request.POST.get("monitorizacion") else u'0'
		ventilacion_mecanica 	= u'3' if request.POST.get("ventilacion_mecanica")	else u'0'
		inmovilizacion			= u'2' if request.POST.get("inmovilizacion") else u'0'
		marcapaso				= u'3' if request.POST.get("marcapaso") else u'0'		
		BIC 					= u'2' if request.POST.get("BIC") else u'0'

		# Choices
		oxigenoterapia 			= request.POST.get("oxigenoterapia")
		acceso_vascular			= request.POST.get("acceso_vascular")
		hemodinamia				= request.POST.get("hemodinamia")
		ventilatorio			= request.POST.get("ventilatorio")
		glasgow					= request.POST.get("glasgow")


		diagnostico = [
			monitorizacion,
			ventilacion_mecanica,
			inmovilizacion,
			marcapaso,
			BIC,
			oxigenoterapia 	if oxigenoterapia.isdigit()  	else u'0',
			acceso_vascular if acceso_vascular.isdigit() 	else u'0',
			hemodinamia 	if hemodinamia.isdigit()  		else u'0',
			ventilatorio 	if ventilatorio.isdigit()  		else u'0',
			glasgow 		if glasgow.isdigit()  			else u'0']

		data['value'] = max(diagnostico)
	
	return HttpResponse(json.dumps(data),content_type='application/json')

def evaluador(request):

	data = {
		'oxigenoterapia' 	: CHOICES_OXIGENOTERAPIA,
		'acceso'			: CHOICES_ACCESO,
		'hemodinamia'		: CHOICES_HEMODINAMIA,
		'ventilatorio'		: CHOICES_VENTILATORIO,
		'glasgow'			: CHOICES_GLASGOW
		}

	return render_to_response('diagnostico.html', data, context_instance=RequestContext(request))


		

