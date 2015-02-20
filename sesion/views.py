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


# Create your views here.
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


def add_user(request):
	return HttpResponseRedirect('/')

def edit_user(request):
	return HttpResponseRedirect('/')

def change_pass(request):
	return HttpResponseRedirect('/')