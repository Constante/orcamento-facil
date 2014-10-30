from django.contrib import admin

# Register your models here.
from .models import *
# from .models import Client
# from .models import Shipping
# from .models import ProductShip
# from .models import Service
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

class ShippingAdmin(admin.ModelAdmin):
	
	# exclude = ('user',)

	list_display = ['__unicode__', 'email' ,'cnpj', 'phone' ]

	class Meta:
		model = Shipping
	
	
	def save_model(self, request, obj, form, change):
		if not change:
			obj.user = request.user
			obj.save()

admin.site.register(Shipping, ShippingAdmin)

class ProductShipAdmin(admin.ModelAdmin):
	
	# exclude = ('user',)
	# inlines = [
		
	# ]

	list_display = ['__unicode__','price', 'deliverydays' ]

	class Meta:
		model = ProductShip
	

admin.site.register(ProductShip, ProductShipAdmin)

class ServiceAdmin(admin.ModelAdmin):

	list_display = ['__unicode__','title','tipo','price','hourprice']

	class Meta:
		model = Service

admin.site.register(Service, ServiceAdmin)

class GuaranteeAdmin(admin.ModelAdmin):

	list_display = ['__unicode__','title']

	class Meta:
		model = Guarantee

admin.site.register(Guarantee, GuaranteeAdmin)

class TermsAdmin(admin.ModelAdmin):

	list_display = ['__unicode__','title']

	class Meta:
		model = Term

admin.site.register(Term, TermsAdmin)