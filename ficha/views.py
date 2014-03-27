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

from forms import FichaForm
from forms import IngresarFichaForm

from ficha.models import Ficha


def index(request):
	return HttpResponseRedirect('/login')

@login_required(login_url='/')
def home(request):
	return render_to_response('base.html', context_instance=RequestContext(request))

@login_required(login_url='/')
def ficha_ingresar(request):

	if request.POST:
		form = FichaForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/ficha/listado')
	else:
		form = FichaForm()

	return render_to_response('ficha.html',{'form':form}, context_instance=RequestContext(request))


@login_required(login_url='/')
def ficha_redirect(request):
    return HttpResponseRedirect('/ficha/listado/1')


@login_required(login_url='/')
def ficha_listado(request, page):
	listado = Ficha.objects.all().order_by('date_start').reverse()
	paginator = Paginator(listado, 2)

	try:
		pages = int(page)
	except:
		pages = 1

	try:
		lista = paginator.page(pages)

	except (InvalidPage):
		lista = paginator.page(paginator.num_pages)

	return render_to_response('ficha_listado.html',{'list':lista}, context_instance=RequestContext(request))


@login_required(login_url='/')
def ficha_ver(request, folio):
	p = Ficha.objects.get(id=folio)
	return render_to_response('ficha_ver.html', {'ficha':p}, context_instance=RequestContext(request))


@login_required(login_url='/')
def ficha_modificar(request, folio):
	p = Ficha.objects.get(id=folio)

	if request.method == 'POST':
		form = FichaForm(request.POST)
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

			p.km_inicio			= form.cleaned_data['km_inicio']
			p.km_termino		= form.cleaned_data['km_termino']
			p.hora_inicio 		= form.cleaned_data['hora_inicio']
			p.hora_llegada		= form.cleaned_data['hora_llegada']
			p.hora_QTH_inicio 	= form.cleaned_data['hora_QTH_inicio']
			p.hora_QTH_final	= form.cleaned_data['hora_QTH_final']


			p.save()
			return HttpResponseRedirect('/ficha/listado')

	if request.method == 'GET':
		form = FichaForm(initial={
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

			'km_inicio'			: p.km_inicio,
			'km_termino'		: p.km_termino,
			'hora_inicio'		: p.hora_inicio,
			'hora_llegada'		: p.hora_llegada,

			'hora_QTH_inicio'	: p.hora_QTH_inicio,
			'hora_QTH_final'	: p.hora_QTH_final,

			})

	return render_to_response('ficha.html',{'form':form}, context_instance=RequestContext(request))

def ingresar(request):

	if not request.user.is_anonymous():
		return HttpResponseRedirect('/home')

	if request.method == 'POST':
		form    = AuthenticationForm(request.POST)
		if form.is_valid:
			username    = request.POST['username']
			password    = request.POST['password']
			access      = authenticate(username=username, password=password)
			if access is not None:
				if access.is_active:
					login(request, access)
					return HttpResponseRedirect('/home')
				else:
					return render_to_response('login.html', context_instance=RequestContext(request))
			else:
				return render_to_response('login.html', context_instance=RequestContext(request))
		else:
			return render_to_response('login.html', context_instance=RequestContext(request))
	else:
		form = AuthenticationForm()
	return render_to_response('login.html', {'formulario':form}, context_instance=RequestContext(request))



@login_required(login_url='/')
def cerrar(request):
	logout(request)
	return HttpResponseRedirect('/')










def ficha_ingresar2(request):
	if request.POST:
		form = IngresarFichaForm(request.POST)
		if form.is_valid():
			a = form.cleaned_data['estado_ficha']

			return HttpResponseRedirect('/ficha/listado')
	else:
		form = IngresarFichaForm()
	return render_to_response('ficha.html',{'form':form}, context_instance=RequestContext(request))




