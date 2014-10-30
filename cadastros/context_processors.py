from django.shortcuts import render, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate

from django.contrib.auth.models import User

from .models import *
# from .models import Client 
# from .models import Shipping 
# from .forms import ClientForm
# from .forms import ProdutoForm
from .forms import *

def add_produtos(request, username=""):
	form_title = 'Cadastro de produto'
	# user = User.objects.get(username=username)
	produto_form = ProdutoForm(request.POST or None)
	user = request.user.id
	produtos = Produto.objects.filter(user=user)
	

	
	if produto_form.is_valid():

		obj = produto_form.save(commit=False)
		obj.user = request.user
		obj.save()
		obj.clean()
	

	return {

	'produto_form': produto_form, 'form_title': form_title, 'produtos':produtos

	}

def add_clients(request):
	
	form_name = 'Cadastre seu cliente'
	form = ClientForm(request.POST or None)
	user = request.user.id
	clients = Client.objects.filter(user=user)


	if form.is_valid():
		obj = form.save(commit=False)
		obj.user = request.user
		obj.save()
		
	
	return {

	'add_clients': form, 'client_name': form_name, 'clients': clients

	} 



def add_shippings(request):
	
	form_name = 'Cadastre transportadora'
	form = ShippingForm(request.POST or None)
	user = request.user.id
	shippings = Shipping.objects.filter(user=user)


	if form.is_valid():
		obj = form.save(commit=False)
		obj.user = request.user
		obj.save()
		
	return {

	'add_shippings': form, 'shipping_name': form_name, 'shippings': shippings

	} 


def add_services(request):
	
	form_name = 'Cadastre o servico'
	form = ServiceForm(request.POST or None)
	user = request.user.id
	services = Service.objects.filter(user=user)


	if form.is_valid():
		obj = form.save(commit=False)
		obj.user = request.user
		obj.save()	
	
	return {

	'add_services': form, 'service_name': form_name, 'services': services

	} 

def add_terms(request):
	
	form_name = 'Cadastre o termo'
	form = TermsForm(request.POST or None)
	user = request.user.id
	terms = Term.objects.filter(user=user)


	if form.is_valid():
		obj = form.save(commit=False)
		obj.user = request.user
		obj.save()	
	
	return {

	'add_terms': form, 'terms_name': form_name, 'terms': terms

	} 
def add_garantias(request):
	
	form_name = 'Cadastre a garantia'
	form = GuaranteeForm(request.POST or None)
	user = request.user.id
	garantias = Guarantee.objects.filter(user=user)


	if form.is_valid():
		obj = form.save(commit=False)
		obj.user = request.user
		obj.save()	
	
	return {

	'add_garantias': form, 'garantia_name': form_name, 'garantias': garantias

	} 