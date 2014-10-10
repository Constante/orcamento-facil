from django.contrib import admin
from models import Cnpj
from forms import CnpjForm

class CnpjAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'cnpj']
	form = CnpjForm


admin.site.register(Cnpj, CnpjAdmin)