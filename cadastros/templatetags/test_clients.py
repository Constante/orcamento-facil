from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django import template

from .models import Client 

from .forms import ClientForm

register = template.Library()

@register.inclusion_tags('add_clients.html')
def test_clients():

	form_name = 'Cadastre seu cliente'
	form = ClientForm(request.POST or None)


	if form.is_valid():
		obj = form.save(commit=False)
		obj.user = request.user
		obj.save()
		return HttpResponseRedirect('')
	

	# template = "add_clients.html"
	context = {'form': form, 'form_name': form_name}
	return context
