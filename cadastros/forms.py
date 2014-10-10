from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
	# def save(self, user, commit=True):
	# 	produto = forms.ModelForm.save(commit=False)
	# 	produto.user = user
	# 	if commit:
	# 		produto.save()
	# 	return produto
	

	class Meta:
		model = Produto
		exclude = ('user',)