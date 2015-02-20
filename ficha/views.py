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
		'causa' 	: CHOICES_CAUSA,
		'movil'		: CHOICES_MOVIL,
		'solicitud'	: CHOICE_SOLICITUD,
		'errors' 	: ''
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
					movil = Movil.objects.filter(apodo="default")[0]
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
def enlista(request):
	listado = Servicio.objects.all()
	return render_to_response('derivaciones_enlista.html',{'servicios':listado}, context_instance=RequestContext(request))

"""
	paginator = Paginator(listado, 10)

	try:
		pages = int(page)
	except:
		pages = 1


	try:
		lista = paginator.page(pages)
	except (InvalidPage):
		lista = paginator.page(paginator.num_pages)

"""





@login_required(login_url='/')
def ficha_redirect(request):
    return HttpResponseRedirect(reverse('listado', args=(1,)))


@login_required(login_url='/')
def ficha_ver(request, folio):
	try:
		id = int(folio)
	except:
		return HttpResponseRedirect(reverse('home'))
	servicio = get_object_or_404(Servicio, id=folio)

	return render_to_response('ver_servicio.html', {'servicio': servicio},
	 context_instance=RequestContext(request))


@login_required(login_url='/')
def ficha_editar(request, folio):

	# Nos aseguramos que de sea un numero 
	try:
		id = int(folio)
	except:
		return HttpResponseRedirect(reverse('home'))
	p = get_object_or_404(Ficha, id=folio)

	# Nos aseguramos que no puedan editar una ficha que ya este archivada
	if p.estado_ficha == ANULADO or p.estado_ficha == FINALIZADO:
		return HttpResponseRedirect(reverse('home'))


	if request.method == 'POST':
		form = EditarFichaForm(request.POST)

		if form.is_valid():

			p.nombre			= form.cleaned_data['nombre']
			p.apellido			= form.cleaned_data['apellido']
			p.rut 				= form.cleaned_data['rut']
			p.edad				= form.cleaned_data['edad']
			p.causa				= form.cleaned_data['causa']
			p.diagnostico		= form.cleaned_data['diagnostico']
			p.observacion		= form.cleaned_data['observacion']


			p.responsable 		= form.cleaned_data['responsable']
			p.telefono			= form.cleaned_data['telefono']
			p.origen			= form.cleaned_data['origen']
			p.medico_derivador 	= form.cleaned_data['medico_derivador']
			p.destino			= form.cleaned_data['destino']
			p.medico_receptor	= form.cleaned_data['medico_receptor']
			

			p.save()
			return HttpResponseRedirect(reverse('home'))

	if request.method == 'GET':
		form = EditarFichaForm(initial={
			'nombre' 			: p.nombre,
			'apellido'			: p.apellido,
			'rut'				: p.rut,
			'edad'				: p.edad,
			'diagnostico'		: p.diagnostico,
			'observacion'		: p.observacion,


			'responsable'		: p.responsable,
			'telefono'			: p.telefono,
			'origen'			: p.origen,
			'medico_derivador' 	: p.medico_derivador,
			'destino'			: p.destino,
			'medico_receptor' 	: p.medico_receptor,

			})

	return render_to_response('ingresar.html',{'form':form}, context_instance=RequestContext(request))


def traslado_agregar(request, folio):

	try:
		id = int(folio)
	except:
		return HttpResponseRedirect(reverse('home'))

	movil 		= Movil.objects.all()
	servicio 	= get_object_or_404(Servicio, id=folio)
	p 			= servicio.traslado


	if request.method == 'POST':
		form = EditarTraslado(request.POST)

		if form.is_valid():

			# Falta agregar una capa de seguridad!! para que no tengamos problemas del estilo...
			# inicio espera > termino espera.
			p.movil				= request.POST.get("movil")
			p.km_inicio			= request.POST.get("km_inicio")
			p.km_termino		= request.POST.get("km_termino")
			p.inicio			= request.POST.get("inicio")
			p.llegada			= request.POST.get("llegada")
			p.inicio_espera		= request.POST.get("inicio_espera")
			p.termino_espera	= request.POST.get("termino_espera")

			p.save()
			return HttpResponseRedirect(reverse('home'))	
	else:

		form = EditarTraslado(initial = {
				'movil' 	: p.movil,
				'km_inicio'	: p.km_inicio,
				'km_termino': p.km_termino,
				'inicio'	: p.inicio,
				'llegada'	: p.llegada,
				'inicio_espera': p.inicio_espera,
				'termino_espera': p.termino_espera,

			})



	return render_to_response('traslado.html', {'form':form, 'movil': movil }, context_instance=RequestContext(request))

"""

@login_required(login_url='/')
def ficha_archivados_redirect(request):
    return HttpResponseRedirect(reverse('archivados', args=(1,)))


@login_required(login_url='/')
def ficha_archivados(request, page):
	listado = Ficha.objects.filter( estado_ficha = ARCHIVO ).order_by('date_start').reverse()
	paginator = Paginator(listado, 10)

	try:
		pages = int(page)
	except:
		pages = 1

	try:
		lista = paginator.page(pages)
	except (InvalidPage):
		lista = paginator.page(paginator.num_pages)


	return render_to_response('lista_archivados.html',{'list':lista}, context_instance=RequestContext(request))




			p.hora_programada	= form.cleaned_data['hora_programada']
			p.km_inicio			= form.cleaned_data['km_inicio']
			p.km_termino		= form.cleaned_data['km_termino']
			p.hora_inicio_Espera 		= form.cleaned_data['hora_inicio_Espera']
			p.hora_llegada_Espera		= form.cleaned_data['hora_llegada_Espera']
			p.hora_QTH_inicio 	= form.cleaned_data['hora_QTH_inicio']
			p.hora_QTH_final	= form.cleaned_data['hora_QTH_final']


			'km_inicio'			: p.km_inicio,
			'km_termino'		: p.km_termino,
			'hora_inicio_Espera': p.hora_inicio_Espera,
			'hora_llegada_Espera': p.hora_llegada_Espera,

			'hora_QTH_inicio'	: p.hora_QTH_inicio,
			'hora_QTH_final'	: p.hora_QTH_final,

def complejidad(request, ficha):

	ficha_objects = get_object_or_404(Ficha, id=ficha)

	if ficha_objects is not None:
		
		if request.POST:
			form = RequerimientosForm(request.POST, initial={'ficha' : ficha })
			if form.is_valid():
				form.save()
				return HttpResponseRedirect(reverse('home'))
		else:
			form = RequerimientosForm(initial={
				'ficha' : ficha 
				})

		return render_to_response('complejidad.html',{'form': form, 'ficha': ficha_objects }, 
			context_instance=RequestContext(request))
	
	else:
		return HttpResponseRedirect(reverse('home'))


"""
