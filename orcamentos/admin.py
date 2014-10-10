from django.contrib import admin

# Register your models here.
from .models import Orcamento

class OrcamentoAdmin(admin.ModelAdmin):
	readonly_fields=('id',)
	class Meta:
		model = Orcamento


admin.site.register(Orcamento, OrcamentoAdmin)

# testando git