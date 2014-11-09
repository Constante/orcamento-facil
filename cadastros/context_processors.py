from django.shortcuts import render, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate

from django.contrib.auth.models import User

from .models import *
from .forms import *


def cadastros(request):
	if request.user.is_authenticated():
		user = request.user.id
		verUser = True
		# Popular os titulos
		ProductFormTitle = 'Cadastre Produto'
		ClientFormTitle = 'Cadastre seu Cliente'
		ShippingFormTitle = 'Cadastre transportadora'
		ServiceFormTitle = 'Cadastre o servico'
		TermsFormTitle = 'Cadastre o termo'
		GuaranteeFormTitle = 'Cadastre a garantia'
		PaymentFormTitle = 'Cadastre o pagamento'
		
		# Popular os forms
		ProductFormContext = ProdutoForm(request.POST or None, prefix="product")
		ClientFormContext = ClientForm(request.POST or None, prefix="client")
		ShippingFormContext = ShippingForm(request.POST or None, prefix="ship")
		ServiceFormContext = ServiceForm(request.POST or None, prefix="serv")
		TermsFormContext = TermsForm(request.POST or None, prefix="term")
		GuaranteeFormContext = GuaranteeForm(request.POST or None, prefix="gar")
		PaymentFormContext = PaymentForm(request.POST or None, prefix="pay")

		# Popular os tables
		produtos = Produto.objects.filter(user=user)
		clientes = Client.objects.filter(user=user)
		shippings = Shipping.objects.filter(user=user)
		services = Service.objects.filter(user=user)
		terms = Term.objects.filter(user=user)
		garantias = Guarantee.objects.filter(user=user)
		payments = Payment.objects.filter(user=user)

		if request.method == 'POST':
			
			if 'add_produto' in request.POST:
				ProductFormContext = ProdutoForm(request.POST or None, prefix="product")
				if ProductFormContext.is_valid():
					obj = ProductFormContext.save(commit=False)
					obj.user = request.user
					obj.save()
					ProductFormContext.clean()
			elif 'add_client' in request.POST:
				ClientFormContext = ClientForm(request.POST or None, prefix="client")
				if ClientFormContext.is_valid():
					obj = ClientFormContext.save(commit=False)
					obj.user = request.user
					obj.save()
					ClientFormContext.clean()
			elif 'add_shipping' in request.POST:
				ShippingFormContext = ShippingForm(request.POST or None, prefix="ship")
				if ShippingFormContext.is_valid():
					obj = ShippingFormContext.save(commit=False)
					obj.user = request.user
					obj.save()
					ShippingFormContext.clean()
			elif 'add_service' in request.POST:
				ServiceFormContext = ServiceForm(request.POST or None, prefix="serv")
				if ServiceFormContext.is_valid():
					obj = ServiceFormContext.save(commit=False)
					obj.user = request.user
					obj.save()
					ServiceFormContext.clean()
			elif 'add_terms' in request.POST:
				TermsFormContext = TermsForm(request.POST or None, prefix="term")
				if TermsFormContext.is_valid():
					obj = TermsFormContext.save(commit=False)
					obj.user = request.user
					obj.save()
					TermsFormContext.clean()
			elif 'add_garantia' in request.POST:
				GuaranteeFormContext = GuaranteeForm(request.POST or None, prefix="gar")
				if GuaranteeFormContext.is_valid():
					obj = GuaranteeFormContext.save(commit=False)
					obj.user = request.user
					obj.save()
					GuaranteeFormContext.clean()
			elif 'add_payment' in request.POST:
				PaymentFormContext = PaymentForm(request.POST or None, prefix="pay")
				if PaymentFormContext.is_valid():
					obj = PaymentFormContext.save(commit=False)
					obj.user = request.user
					obj.save()
					PaymentFormContext.clean()
		return {
		'verUser':verUser,
		'produto_form': ProductFormContext, 'form_title': ProductFormTitle,'produtos': produtos,
		'client_form': ClientFormContext, 'client_title': ClientFormTitle,'clientes': clientes,
		'ship_form': ShippingFormContext, 'ship_title': ShippingFormTitle,'shippings': shippings,
		'service_form': ServiceFormContext, 'service_title': ServiceFormTitle,'services': services,
		'term_form': TermsFormContext, 'term_title': TermsFormContext,
		'guarantee_form': GuaranteeFormContext, 'guarantee_title': GuaranteeFormTitle,'guarantees': garantias,
		'payment_form': PaymentFormContext, 'payment_title': PaymentFormTitle,'payments': payments,
		}
	else:

		verUser = False
		print verUser
		padrao = "Voce precisa estar logado para ver isso."
		return {
		'padrao':padrao
		}




# def add_produtos(request, username=""):
# 	# form_title = 'Cadastro de produto'
# 	# # user = User.objects.get(username=username)
# 	# produto_form = ProdutoForm(request.POST or None, prefix="prod")
# 	# user = request.user.id
# 	# produtos = Produto.objects.filter(user=user)
# 	# if produto_form.is_valid():

# 	# 	obj = produto_form.save(commit=False)
# 	# 	obj.user = request.user
# 	# 	obj.save()
# 	# 	obj.clean()
	

# 	return {

# 	# 'produto_form': produto_form, 'form_title': form_title, 'produtos':produtos

# 	}
# def add_clients(request):
	
# 	# form_name = 'Cadastre seu cliente'
# 	# form = ClientForm(request.POST or None, prefix="client")
# 	# user = request.user.id
# 	# clients = Client.objects.filter(user=user)


# 	# if form.is_valid():
# 	# 	obj = form.save(commit=False)
# 	# 	obj.user = request.user
# 	# 	obj.save()
		
	
# 	return {

# 	# 'add_clients': form, 'client_name': form_name, 'clients': clients

# 	} 
# def add_shippings(request):
	
# 	# form_name = 'Cadastre transportadora'
# 	# form = ShippingForm(request.POST or None, prefix="ship")
# 	# user = request.user.id
# 	# shippings = Shipping.objects.filter(user=user)


# 	# if form.is_valid():
# 	# 	obj = form.save(commit=False)
# 	# 	obj.user = request.user
# 	# 	obj.save()
		
# 	return {

# 	# 'add_shippings': form, 'shipping_name': form_name, 'shippings': shippings

# 	} 
# def add_services(request):
	
# 	# form_name = 'Cadastre o servico'
# 	# form = ServiceForm(request.POST or None, prefix="serv")
# 	# user = request.user.id
# 	# services = Service.objects.filter(user=user)


# 	# if form.is_valid():
# 	# 	obj = form.save(commit=False)
# 	# 	obj.user = request.user
# 	# 	obj.save()	
	
# 	return {

# 	# 'add_services': form, 'service_name': form_name, 'services': services

# 	} 
# def add_terms(request):
	
# 	form_name = 'Cadastre o termo'
# 	form = TermsForm(request.POST or None, prefix="term")
# 	user = request.user.id
# 	terms = Term.objects.filter(user=user)


# 	if form.is_valid():
# 		obj = form.save(commit=False)
# 		obj.user = request.user
# 		obj.save()	
	
# 	return {

# 	'add_terms': form, 'terms_name': form_name, 'terms': terms

# 	} 
# def add_garantias(request):
# 	form_name = 'Cadastre o termo'
# 	form_name = 'Cadastre a garantia'
# 	form = GuaranteeForm(request.POST or None, prefix="gar")
# 	user = request.user.id
# 	garantias = Guarantee.objects.filter(user=user)


# 	if form.is_valid():
# 		obj = form.save(commit=False)
# 		obj.user = request.user
# 		obj.save()	
	
# 	return {

# 	'add_garantias': form, 'garantia_name': form_name, 'garantias': garantias

# 	} 
# def add_geral(request):
# 	print request
# 	return
