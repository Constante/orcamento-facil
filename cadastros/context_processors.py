from django.shortcuts import render, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate

from django.contrib.auth.models import User

from .models import Produto
from .models import Client 
from .forms import ClientForm
from .forms import ProdutoForm

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

	'add_clients': form, 'form_name': form_name, 'clients': clients

	} 



