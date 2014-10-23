from django.contrib import admin

# Register your models here.
from .models import Produto
from .models import Client
from forms import ClientForm
# from .models import Person

class ProdutoAdmin(admin.ModelAdmin):
	
	# exclude = ('user',)

	class Meta:
		model = Produto
	
	def save_model(self, request, obj, form, change):
		if not change:
			obj.user = request.user
		obj.save()

admin.site.register(Produto, ProdutoAdmin)


# class PersonAdmin(admin.ModelAdmin):
# 	class Meta:
# 		model = Person

# admin.site.register(Person, PersonAdmin)

class ClientAdmin(admin.ModelAdmin):
	
	# exclude = ('user',)

	
	list_display = ['__unicode__', 'cpf', 'cnpj', 'user']
	form = ClientForm
	
	
	def save_model(self, request, obj, form, change):
		if not change:
			obj.user = request.user
		obj.save()

admin.site.register(Client, ClientAdmin)
