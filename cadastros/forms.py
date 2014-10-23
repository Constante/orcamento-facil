from django.forms import ModelForm
from django import forms
from .models import Produto
from .models import Client
from localflavor.br.forms import BRStateSelect
from localflavor.br.forms import BRPhoneNumberField
from localflavor.br.forms import BRZipCodeField
from localflavor.br.forms import BRCPFField
from django_localflavor_br.forms import BRCNPJField
from django_localflavor_br.forms import BRPhoneNumberField
from django_countries.widgets import CountrySelectWidget


class ProdutoForm(ModelForm):
	# def save(self, user, commit=True):
	# 	produto = forms.ModelForm.save(commit=False)
	# 	produto.user = user
	# 	if commit:
	# 		produto.save()
	# 	return produto
	

	class Meta:
		model = Produto
		exclude = ('user',)


class ClientForm(forms.ModelForm):
	
	


	class Meta:
		model = Client
		form = Client
		widgets = { 'state': BRStateSelect(),'country': CountrySelectWidget() }
		fields = ['name', 'cpf', 'phone', 'cep', 'cnpj', 'state']
	
	
	cpf = BRCPFField()
	cep = BRZipCodeField(required=True)
	cnpj = BRCNPJField(label='CNPJ', required=False)
	phone = BRPhoneNumberField(label='Telefone')