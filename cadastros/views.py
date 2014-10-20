from django.shortcuts import render, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django_tables2   import RequestConfig
from .models import Produto 
# from .models import Person

from .forms import ProdutoForm


from django.forms.models import modelformset_factory
from django.forms.models import inlineformset_factory

from django import template
register = template.Library()
# Create your views here.

def cadastros(request):
	user = request.user
	produtos = Produto.objects.filter(user=user)
	template = 'cadastros.html'
	
	context = {'produtos': produtos,}
	produto_form = ProdutoForm(request.POST or None)

	

	return render(request, template, context)



def add_produtos(request, username=""):
	form_title = 'Cadastro de produto'
	user = User.objects.get(username=username)
	# ProdutoInlineFormSet = inlineformset_factory(Produto, form=ProdutoForm)
	form = ProdutoForm(prefix="A")
	produto_form = ProdutoForm(request.POST or None, prefix="A")
	produtos = Produto.objects.filter(user=user)
	single_user = user

	
	
	if request.user.username == username:

		if produto_form.is_valid():

			obj = produto_form.save(commit=False)
			obj.user = request.user
			obj.save()
			return HttpResponseRedirect('')
		


	else:
		raise Http404


	template = 'add_produtos.html'

	context = {'single_user': single_user, 'produto_form': produto_form, 'form_title': form_title, 'produtos':produtos}

	return render(request, template, context)





def delete_produtos(request,id):
	username = request.user.username
	

	produtoid = Produto.objects.get(id=id)
	produtoid.delete()
	return HttpResponseRedirect(reverse('add_produtos', kwargs={'username': username}))


def edit_produtos(request, id):
	
	username = request.user

	produtoid = Produto.objects.filter(user=username)
	instance = Produto.objects.get(id=id)
	
	form = ProdutoForm(request.POST or None, instance=instance)

	if form.is_valid():
		produto_edit = form.save()
		return HttpResponseRedirect(reverse('add_produtos', kwargs={'username': username}))

	template = "single_produto.html"
	context = {"produtoid": produtoid, "edit": True, "form": form, }

	return render(request, template, context)

