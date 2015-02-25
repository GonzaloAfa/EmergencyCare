# -*- encoding: utf-8 -*-
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

from ficha.forms import *
from ficha.models import *

from diagnostico.models import CHOICES_OXIGENOTERAPIA, CHOICES_ACCESO, CHOICES_HEMODINAMIA, CHOICES_VENTILATORIO, CHOICES_GLASGOW


def index(request):
	return HttpResponseRedirect(reverse('login'))

@login_required(login_url='/')
def home(request):
	return render_to_response('base.html', context_instance=RequestContext(request))



@login_required(login_url='/')
def ficha_ingresar(request):

	valid = True
	errors = {}

	data = {
		'causa' 			: CHOICES_CAUSA,
		'movil'				: CHOICES_MOVIL,
		'solicitud'			: CHOICE_SOLICITUD,
		'errors' 			: '',
		'oxigenoterapia' 	: CHOICES_OXIGENOTERAPIA,
		'acceso'			: CHOICES_ACCESO,
		'hemodinamia'		: CHOICES_HEMODINAMIA,
		'ventilatorio'		: CHOICES_VENTILATORIO,
		'glasgow'			: CHOICES_GLASGOW,		
	}

	if request.POST:

		#Datos del paciente
		nombre 		= request.POST.get("nombre")
		apellido 	= request.POST.get("apellido")
		rut 		= request.POST.get("rut")
		edad 		= request.POST.get("edad")
		causa 		= request.POST.get("causa")
		diagnostico = request.POST.get("diagnostico")
		observacion = request.POST.get("observacion")

		#Datos gravedad del paciente
		tipo_movil 	= request.POST.get("tipo_movil")

		#Datos del traslado
		responsable 		= request.POST.get("responsable")
		telefono			= request.POST.get("telefono")
		origen				= request.POST.get("origen")
		medico_derivador 	= request.POST.get("medico_derivador")
		destino				= request.POST.get("destino")
		medico_receptor		= request.POST.get("medico_receptor")

		solicitud			= request.POST.get("solicitud")
		hora_programada		= request.POST.get("hora_programada")

		# Validar
		if nombre and apellido and edad and causa and tipo_movil and responsable and telefono and origen and medico_derivador and destino and medico_receptor and solicitud:
			ficha = Ficha.objects.create(
					nombre			= nombre,
					apellido 		= apellido,
					rut				= rut,
					edad			= edad, 			
					causa  			= causa, 
					diagnostico		= diagnostico, 
					observacion		= observacion, 	

					tipo_movil 		=  tipo_movil,
					
					responsable 	= responsable,
					telefono		= telefono,
					origen			= origen,
					medico_derivador= medico_derivador,
					destino			= destino,
					medico_receptor	= medico_receptor
					)
			ficha.save()

			traslado = Traslado.objects.create(
					movil = Movil.objects.filter(apodo="default")[0],
					estado_traslado = SALIRBASE,
					)
			traslado.save()


			if solicitud == '1':

				servicio = Servicio.objects.create(
					estado_ficha	= ENLISTADO,
					solicitud 		= solicitud,
					hora_programada = hora_programada,
					ficha 			= ficha,
					traslado 		= traslado
					)

			elif solicitud == '2':
				servicio = Servicio.objects.create(
					estado_ficha	= ENLISTADO,
					solicitud 		= solicitud,
					ficha 			= ficha,
					traslado 		= traslado
					)

			return HttpResponseRedirect(reverse('enlista'))

		else:
			data = {
				'causa' 	: CHOICES_CAUSA,
				'movil'		: CHOICES_MOVIL,
				'solicitud'	: CHOICE_SOLICITUD,
				'errors' 	: 'Existen campos vacios'
			}
			return render_to_response('ingresar_servicio.html', data, 
				context_instance=RequestContext(request))

	
	return render_to_response('ingresar_servicio.html', data, 
		context_instance=RequestContext(request))



@login_required(login_url='/')
def enlista(request, page):
	listado = Servicio.objects.all().order_by('-id')

	paginator = Paginator(listado, 3)

	try:
		pages = int(page)
	except:
		pages = 1


	try:
		lista = paginator.page(pages)
	except (InvalidPage):
		lista = paginator.page(paginator.num_pages)


	data = {
		'servicios' : lista,
		'ENLISTADO'	: ENLISTADO,
		'ENCURSO' 	: ENCURSO,
		'FINALIZADO': FINALIZADO,
		'ANULADO' 	: ANULADO,
		}

	return render_to_response('derivaciones_enlista.html',data, context_instance=RequestContext(request))






@login_required(login_url='/')
def ficha_redirect(request):
    return HttpResponseRedirect(reverse('listado', kwargs={'page' : 1} ))


@login_required(login_url='/')
def ficha_ver(request, folio):
	try:
		id = int(folio)
	except:
		return HttpResponseRedirect(reverse('home'))
	servicio = get_object_or_404(Servicio, id=folio)

	return render_to_response('ver_servicio.html', {'servicio': servicio},
	 context_instance=RequestContext(request))



def traslado_agregar(request, folio):

	try:
		id = int(folio)
	except:
		return HttpResponseRedirect(reverse('home'))

	movil 		= Movil.objects.all()
	servicio 	= get_object_or_404(Servicio, id=folio)
	p 			= servicio.traslado
	error 		= ''
	status 		= { 
				'SALIRBASE' 	: SALIRBASE,
				'CONTACTO' 		: CONTACTO,
				'INICIOTRASLADO': INICIOTRASLADO,
				'FINTRASLADO' 	: FINTRASLADO,
				'ENTREGA' 		: ENTREGA,
				'ENLISTADO' 	: ENLISTADO,
				'ENCURSO'		: ENCURSO,

				}


	if request.method == 'POST':


		if servicio.estado_ficha == str(ENLISTADO):

			if p.estado_traslado == SALIRBASE:

				movil 				= get_object_or_404(Movil,pk= request.POST.get("movil"))
				km_inicio			= request.POST.get("km_inicio")

				if km_inicio is not None:
					p.movil				= movil
					p.km_inicio			= request.POST.get("km_inicio")
					p.estado_traslado 	= CONTACTO

					servicio.estado_ficha = ENCURSO
					servicio.save()
				else:

					error 			= "Ingrese una fecha válida"
					return render_to_response('traslado.html', 
						{'movil': movil, 'status' : status, 'servicio':servicio, 'error' : error }, 
						context_instance=RequestContext(request))


			elif p.estado_traslado == CONTACTO:

				p.contacto_paciente	= request.POST.get("contacto_paciente")
				p.estado_traslado 	= INICIOTRASLADO

	
			elif p.estado_traslado == INICIOTRASLADO:

				p.inicio_traslado	= request.POST.get("inicio_traslado")
				p.estado_traslado 	= FINTRASLADO


			elif p.estado_traslado == FINTRASLADO:

				p.fin_traslado		= request.POST.get("fin_traslado")
				p.km_termino 		= request.POST.get("km_termino")
				p.estado_traslado 	= ENTREGA

			elif p.estado_traslado == ENTREGA:
				p.entrega_paciente	= request.POST.get("entrega_paciente")
				servicio.estado_ficha = FINALIZADO
				servicio.save()



			# Falta agregar una capa de seguridad!! para que no tengamos problemas del estilo...
			# inicio espera > termino espera.

			p.save()
			return HttpResponseRedirect(reverse('home'))	
		else:
			error = "Estás tratando de agregar informacion de traslado a un servicio que fue anulado o ya finalizó"


	else:
		error = "Existe un problema"

	return render_to_response('traslado.html', {'movil': movil, 'status' : status, 'servicio':servicio, 'error' : error }, context_instance=RequestContext(request))