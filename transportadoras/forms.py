# -*- coding: utf-8 -*-
from django import forms
from django_localflavor_br.forms import BRCNPJField
from models import Cnpj


class CnpjForm(forms.ModelForm):
	
	cnpj = BRCNPJField(label='CNPJ', required=False)
    
class Meta:
	model = Cnpj

