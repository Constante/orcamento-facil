from django.shortcuts import render, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django_tables2   import RequestConfig
from .models import Produto
from .models import Client 
# from .models import Person

from .forms import ProdutoForm
from .forms import ClientForm


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
