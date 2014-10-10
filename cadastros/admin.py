from django.contrib import admin

# Register your models here.
from .models import Produto

class ProdutoAdmin(admin.ModelAdmin):
	
	# exclude = ('user',)

	class Meta:
		model = Produto
	
	def save_model(self, request, obj, form, change):
		if not change:
			obj.user = request.user
		obj.save()

admin.site.register(Produto, ProdutoAdmin)