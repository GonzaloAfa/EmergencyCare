from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext


#autentificacion
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

#paginator
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import InvalidPage

from django.core.context_processors import csrf

from forms import FichaForm, RequerimientosForm
from forms import EditarFichaForm

from ficha.models import Ficha
from ficha.models import ARCHIVO, PROGRAMADO, PROCESO

#usar name url para redireccionar
from django.core.urlresolvers import reverse

from django.db.models import Q

def index(request):
	return HttpResponseRedirect(reverse('login'))

@login_required(login_url='/')
def home(request):
	return render_to_response('base.html', context_instance=RequestContext(request))

@login_required(login_url='/')
def ficha_ingresar(request):
	if request.POST:
		form = FichaForm(request.POST)
		if form.is_valid():
			nueva_ficha = form.save()
			return HttpResponseRedirect(reverse('evaluador', args=(nueva_ficha.pk,)))
	else:
		form = FichaForm()

	return render_to_response('ingresar.html',{'form':form}, context_instance=RequestContext(request))


@login_required(login_url='/')
def ficha_redirect(request):
    return HttpResponseRedirect(reverse('listado', args=(1,)))

@login_required(login_url='/')
def ficha_archivados_redirect(request):
    return HttpResponseRedirect(reverse('archivados', args=(1,)))


@login_required(login_url='/')
def ficha_listado(request, page):
	listado = Ficha.objects.filter( Q(estado_ficha = PROGRAMADO) | Q(estado_ficha = PROCESO)  ).order_by('date_start').reverse()
	paginator = Paginator(listado, 10)

	try:
		pages = int(page)
	except:
		pages = 1


	try:
		lista = paginator.page(pages)
	except (InvalidPage):
		lista = paginator.page(paginator.num_pages)


	return render_to_response('lista_fichas.html',{'list':lista}, context_instance=RequestContext(request))



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


@login_required(login_url='/')
def ficha_ver(request, folio):
	p = Ficha.objects.get(id=folio)
	return render_to_response('visualizar.html', {'ficha':p}, context_instance=RequestContext(request))


@login_required(login_url='/')
def ficha_modificar(request, folio):

	# Nos aseguramos que de sea un numero 
	try:
		id = int(folio)
	except:
		return HttpResponseRedirect(reverse('home'))


	p = get_object_or_404(Ficha, id=folio)

	# Nos aseguramos que no puedan editar una ficha que ya este archivada
	if p.estado_ficha == ARCHIVO:
		return HttpResponseRedirect(reverse('home'))


	if request.method == 'POST':
		form = EditarFichaForm(request.POST)
		if form.is_valid():
			p.estado_ficha 		= form.cleaned_data['estado_ficha']
			p.nombre			= form.cleaned_data['nombre']
			p.apellido			= form.cleaned_data['apellido']
			p.rut 				= form.cleaned_data['rut']
			p.edad				= form.cleaned_data['edad']
			p.sexo				= form.cleaned_data['sexo']
			p.diagnostico		= form.cleaned_data['diagnostico']
			
			p.responsable		= form.cleaned_data['responsable']
			p.telefono			= form.cleaned_data['telefono']
			p.origen			= form.cleaned_data['origen']
			p.medico_derivador 	= form.cleaned_data['medico_derivador']
			p.destino			= form.cleaned_data['destino']
			p.medico_receptor	= form.cleaned_data['medico_receptor']
			p.causa				= form.cleaned_data['causa']
			
			p.tipo_movil		= form.cleaned_data['tipo_movil']

			p.hora_programada	= form.cleaned_data['hora_programada']
			p.km_inicio			= form.cleaned_data['km_inicio']
			p.km_termino		= form.cleaned_data['km_termino']
			p.hora_inicio_Espera 		= form.cleaned_data['hora_inicio_Espera']
			p.hora_llegada_Espera		= form.cleaned_data['hora_llegada_Espera']
			p.hora_QTH_inicio 	= form.cleaned_data['hora_QTH_inicio']
			p.hora_QTH_final	= form.cleaned_data['hora_QTH_final']


			p.save()
			return HttpResponseRedirect(reverse('home'))

	if request.method == 'GET':
		form = EditarFichaForm(initial={
			'estado_ficha'		: p.estado_ficha,
			'nombre' 			: p.nombre,
			'apellido'			: p.apellido,
			'rut'				: p.rut,
			'edad'				: p.edad,
			'sexo'				: p.sexo,
			'diagnostico'		: p.diagnostico,

			'responsable'		: p.responsable,
			'telefono'			: p.telefono,
			'origen'			: p.origen,
			'medico_derivador' 	: p.medico_derivador,
			'destino'			: p.destino,
			'medico_receptor' 	: p.medico_receptor,
			'causa'				: p.causa,

			'tipo_movil'		: p.tipo_movil,
			'hora_programada'	: p.hora_programada,

			'km_inicio'			: p.km_inicio,
			'km_termino'		: p.km_termino,
			'hora_inicio_Espera': p.hora_inicio_Espera,
			'hora_llegada_Espera': p.hora_llegada_Espera,

			'hora_QTH_inicio'	: p.hora_QTH_inicio,
			'hora_QTH_final'	: p.hora_QTH_final,

			})
	return render_to_response('ingresar.html',{'form':form}, context_instance=RequestContext(request))


@login_required(login_url='/')
def cerrar(request):
	logout(request)
	return HttpResponseRedirect('/')


def user_login(request):

	if not request.user.is_anonymous():
		return HttpResponseRedirect(reverse('home'))

	if request.method == 'POST':

		username = request.POST['username']
		password = request.POST['password']

		access = authenticate(username=username, password=password)

		if access is not None:
			if access.is_active:

				login(request, access)
				return HttpResponseRedirect(reverse('home'))
			else:
				return HttpResponseRedirect('/')
		else:
			print "Invalid login details: {0}, {1}".format(username, password)
			return HttpResponseRedirect('/')

	else:
		return render_to_response('login.html', context_instance=RequestContext(request))

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
