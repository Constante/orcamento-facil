from django.shortcuts import render, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django_tables2   import RequestConfig
from .models import Produto 
# from .models import Person
from .tables  import ProdutoTable

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


# def edit_produtos(request):
# 	user = request.user
# 	# produtos = Produto.objects.get(user=user)
# 	# ProdutoFormset = modelformset_factory(Produto, form=ProdutoFormset, extra=1)
# 	# user = request.user
# 	# instance = Produto.objects.get()
	
# 	# user = User.objects.get(username=username) 


# 	produto_form = ProdutoForm(request.POST or None)

# 	context = {'produto_form': produto_form,}

# 	template = 'edit_produtos.html'


# 	return render(request, template, context)


# def edit_produtos(request, username):
# 	try:
# 		user = User.objects.get(username=username)
		

# 		if request.user.is_authenticated():
# 			single_user = user
# 			produto_form = ProdutoForm(request.POST or None)
# 			obj = produto_form.save(commit=False)
# 			obj.user = request.user
# 			obj.save()

			

				
# 	except:
# 		raise Http404

# 	# context = {'produto_form': produto_form,}

# 	template = 'edit_produtos.html'

# 	context = {'single_user': single_user, 'produto_form': produto_form}

# 	return render(request, template, context)


# def edit_produtos(request, username):
	
# 	user = User.objects.get(username=username)
# 	produto_form = ProdutoForm(request.POST or None)
# 	single_user = user

# 	if produto_form.is_valid():

# 		obj = produto_form.save(commit=False)
# 		obj.user = request.user
# 		obj.save()
# 		return HttpResponseRedirect('')
		

				
	

# 	# context = {'produto_form': produto_form,}

# 	template = 'edit_produtos.html'

# 	context = {'single_user': single_user, 'produto_form': produto_form}

# 	return render(request, template, context)

# def edit_produtos(request, username=''):
	
# 	form_title = 'Cadastro de produto'
# 	user = User.objects.get(username=username)
# 	produto_form = ProdutoForm(request.POST or None)
# 	produser = Produto.objects.filter(user=user)
# 	single_user = user
	
# 	table = ProdutoTable(Produto.objects.filter(user=user))
# 	RequestConfig(request).configure(table)
# 	RequestConfig(request, paginate={"per_page": 10}).configure(table)

# 	# @login_required
# 	if request.user.username == username:

# 		if produto_form.is_valid():

# 			obj = produto_form.save(commit=False)
# 			obj.user = request.user
# 			obj.save()
# 			return HttpResponseRedirect('')

# 	else:
# 		raise Http404
		

				
	

# 	# context = {'produto_form': produto_form,}

# 	template = 'edit_produtos.html'

# 	context = {'single_user': single_user, 'produto_form': produto_form, "table": table, 'form_title': form_title,}

# 	return render(request, template, context)


# def people(request):
# 	table = PersonTable(Produto.objects.all())
# 	RequestConfig(request).configure(table)
# 	RequestConfig(request, paginate={"per_page": 10}).configure(table)


# 	return render(request, "people.html", {"table": table})

# def produto_table(request):
# 	table = ProdutoTable(Produto.objects.all())
# 	RequestConfig(request).configure(table)
# 	RequestConfig(request, paginate={"per_page": 10}).configure(table)


# 	return render(request, "edit_produtos", {"table": table})
def add_produtos(request, username=""):
	form_title = 'Cadastro de produto'
	user = User.objects.get(username=username)
	# ProdutoInlineFormSet = inlineformset_factory(Produto, form=ProdutoForm)
	form = ProdutoForm(prefix="A")
	produto_form = ProdutoForm(request.POST or None, prefix="A")
	produtos = Produto.objects.filter(user=user)
	single_user = user

	
	# table = ProdutoTable(Produto.objects.filter(user=user))
	# RequestConfig(request).configure(table)
	# RequestConfig(request, paginate={"per_page": 10}).configure(table)

	# @login_required
	if request.user.username == username:

		if produto_form.is_valid():

			obj = produto_form.save(commit=False)
			obj.user = request.user
			obj.save()
			return HttpResponseRedirect('')
		


	else:
		raise Http404
	# if request.user.username == username:

	# 	u = Produto.objects.filter(user=request.user).get(pk=id).delete()
	# 	return HttpResponseRedirect('')
	

	# context = {'produto_form': produto_form,}

	template = 'add_produtos.html'

	context = {'single_user': single_user, 'produto_form': produto_form, 'form_title': form_title, 'produtos':produtos}

	return render(request, template, context)





def delete_produtos(request,id):
	username = request.user.username
	
	# if request.user.username == username:
	produtoid = Produto.objects.get(id=id)
	produtoid.delete()
	return HttpResponseRedirect(reverse('add_produtos', kwargs={'username': username}))
	# else:
	# 	raise Http404

# template = 'delete_produtos.html'	
# context = {}
# return render(request, template, context)

def edit_produtos(request, id):
	# username = request.user.username
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


@register.inclusion_tag("table_produtos.html")
def table_produtos(request):
	produtos = Produto.objects.all()
	template = 'table_produtos.html'
	context = {'produtos':produtos,}

	
	
	return render(request, template, context)
