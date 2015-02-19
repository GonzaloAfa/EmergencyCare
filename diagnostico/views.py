from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

#autentificacion
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

#paginator
from django.core.paginator import Paginator, EmptyPage, InvalidPage

#usar name url para redireccionar
from django.core.urlresolvers import reverse
from django.db.models import Q

from django.core.context_processors import csrf


def diagnostico(request):

	if request.POST:

		# Boolean
		monitorizacion 			= 2 if request.POST.get("monitorizacion") else 0
		ventilacion_mecanica 	= 3 if request.POST.get("ventilacion_mecanica")	else 0
		inmovilizacion			= 2 if request.POST.get("inmovilizacion") else 0
		marcapaso				= 3 if request.POST.get("marcapaso") else 0		
		BIC 					= 2 if request.POST.get("BIC") else 0

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

			oxigenoterapia 	if oxigenoterapia.isdigit()  	else 0,
			acceso_vascular if acceso_vascular.isdigit() 	else 0,
			hemodinamia 	if hemodinamia.isdigit()  		else 0,
			ventilatorio 	if ventilatorio.isdigit()  		else 0,
			glasgow 		if glasgow.isdigit()  			else 0]

		return max(diagnostico)
	else
		return 0



		

