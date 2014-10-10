from django.shortcuts import render, Http404, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Produto 

from .forms import ProdutoForm


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

def edit_produtos(request, username=''):
	
	user = User.objects.get(username=username)
	produto_form = ProdutoForm(request.POST or None)
	produser = Produto.objects.filter(user=user)
	single_user = user
	
	# @login_required
	if request.user.username == username:

		if produto_form.is_valid():

			obj = produto_form.save(commit=False)
			obj.user = request.user
			obj.save()
			return HttpResponseRedirect('')

	else:
		raise Http404
		

				
	

	# context = {'produto_form': produto_form,}

	template = 'edit_produtos.html'

	context = {'single_user': single_user, 'produto_form': produto_form}

	return render(request, template, context)