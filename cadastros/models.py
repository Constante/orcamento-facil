from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Produto(models.Model):
	user = models.ForeignKey(User,related_name='produtos' ,null=True, blank=True)
	title = models.CharField(max_length=50, verbose_name='produto')
	description = models.CharField(max_length=500, blank=True, verbose_name='decricao')
	price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='preco')


	def __unicode__(self):
		return self.title



class Person(models.Model):
	name = models.CharField(max_length = 50, verbose_name='full name')

	def __unicode__(self):
		return self.name