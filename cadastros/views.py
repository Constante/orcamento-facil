from django.shortcuts import render, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django_tables2   import RequestConfig
# from .models import Produto
# from .models import Client
# from .models import Shipping 
# from .models import ProductShip  
# from .models import Person
from .models import *

from .forms import *
# from .forms import ClientForm
# from .forms import ShippingForm
# from .forms import ProductShipForm

from django.forms.models import modelformset_factory
from django.forms.models import inlineformset_factory

from django import template
register = template.Library()


# Create your views here.

def cadastros(request):
	# username = request.user
	# user = User.objects.get(username=username)

	if request.user.is_authenticated():
		template = 'cadastros.html'

		template_name = 'add_clients.html'

		context = {'template_name': template_name }
		# context['form'] = ClientForm()
		# context['produto_form'] = ProdutoForm()
		return render(request, template, context)
	else:
		raise Http404


	

def add_produtos(request, username=""):
	form_title = 'Cadastro de produto'
	# user = User.objects.get(username=username)
	produto_form = ProdutoForm(request.POST or None, prefix="A")
	user = User.objects.get(username=username)
	produtos = Produto.objects.filter(user=user)

	single_user = user

	if produto_form.is_valid():

		obj = produto_form.save(commit=False)
		obj.user = request.user
		obj.save()
		return HttpResponseRedirect('')
	

	template = 'add_produtos.html'

	context = {'single_user': single_user, 'produto_form': produto_form, 'form_title': form_title, 'produtos':produtos}

	return render(request, template, context)





def delete_produtos(request,id):
	username = request.user.username
	

	produtoid = Produto.objects.get(id=id)
	produtoid.delete()
	return HttpResponseRedirect(reverse('cadastros'))


def edit_produtos(request, id):
	
	username = request.user

	
	produtoid = Produto.objects.filter(user=username)
	instance = Produto.objects.get(id=id)
	
	form = ProdutoForm(request.POST or None, instance=instance)

	if form.is_valid():
		produto_edit = form.save()
		return HttpResponseRedirect(reverse('cadastros'))

	template = "single_produto.html"
	context = {"produtoid": produtoid, "edit": True, "form": form, }

	return render(request, template, context)


def add_clients(request):
	
	form_name = 'Cadastre seu cliente'
	form = ClientForm(request.POST or None)


	if form.is_valid():
		obj = form.save(commit=False)
		obj.user = request.user
		obj.save()
		return HttpResponseRedirect('')
	

	template = "add_clients.html"
	context = {'form': form, 'form_name': form_name}

	return render(request, template, context)

def edit_clients(request, id):
	
	username = request.user

	
	clientid = Client.objects.filter(user=username)
	instance = Client.objects.get(id=id)
	
	form = ClientForm(request.POST or None, instance=instance)

	if form.is_valid():
		client_edit = form.save()
		return HttpResponseRedirect(reverse('cadastros'))

	template = "edit_clients.html"
	context = {"clientid": clientid, "edit": True, "form": form, }

	return render(request, template, context)


def delete_clients(request,id):
	username = request.user.username
	

	clientid = Client.objects.get(id=id)
	clientid.delete()
	return HttpResponseRedirect(reverse('cadastros'))



def add_shippings(request):

	form_name = 'Cadastre seu cliente'
	form = ShippingForm(request.POST or None)


	if form.is_valid():
		obj = form.save(commit=False)
		obj.user = request.user
		obj.save()
		return HttpResponseRedirect('')
	

	template = "add_shippings.html"
	context = {'form': form, 'form_name': form_name}

	return render(request, template, context)

def edit_shippings(request, id):
	
	username = request.user

	
	shippingid = Shipping.objects.filter(user=username)
	instance = Shipping.objects.get(id=id)
	
	form = ShippingForm(request.POST or None, instance=instance)

	if form.is_valid():
		client_edit = form.save()
		return HttpResponseRedirect(reverse('cadastros'))

	template = "edit_shippings.html"
	context = {"shippingid": shippingid, "edit": True, "form": form, }

	return render(request, template, context)

def delete_shippings(request,id):
	username = request.user.username
	

	shippingid = Shipping.objects.get(id=id)
	shippingid.delete()
	return HttpResponseRedirect(reverse('cadastros'))

# def add_productshippings(request):

# 	ps_name = 'Cadastre seu frete'
# 	formset = ProductShipFormset(request.POST or None)


# 	if form.is_valid():
# 		obj = formset.save(commit=False)
# 		obj.user = request.user
# 		obj.save()
# 		return HttpResponseRedirect('')
	

# 	template = "add_shippings.html"
# 	context = {'formset': formset, 'ps_name': ps_name}

# 	return render(request, template, context)

def add_services(request):
	form_name = 'Cadastre seus servicos'
	form = ServiceForm(request.POST or None)

	if form.is_valid():
		obj = form.save(commit=False)
		obj.user = request.user
		obj.save()
		return HttpResponseRedirect('')

	template = "add_services.html"
	context = {'service': form, 'service_name': form_name}

	return render(request, template, context)

def add_terms(request):
	form_name = 'Cadastre seus termos'
	form = TermsForm(request.POST or None)

	if form.is_valid():
		obj = form.save(commit=False)
		obj.user = request.user
		obj.save()
		return HttpResponseRedirect('')

	template = "add_terms.html"
	context = {'add_terms': form, 'term_name': form_name}

	return render(request, template, context)

def add_garantia(request):
	form_name = 'Cadastre suas garantias'
	form = GuaranteeForm(request.POST or None)

	if form.is_valid():
		obj = form.save(commit=False)
		obj.user = request.user
		obj.save()
		return HttpResponseRedirect('')

	template = "add_garantia.html"
	context = {'garantia': form, 'garantia_name': form_name}

	return render(request, template, context)
