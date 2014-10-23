from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

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

class Client(models.Model):
	user = models.ForeignKey(User,null=True, blank=True)
	name = models.CharField(max_length=50, verbose_name='nome')
	lastname = models.CharField(max_length=50)
	cnpj = models.CharField(max_length=20, null=True,blank=False)
	cpf = models.CharField(max_length=20)
	companyname = models.CharField(max_length=20)
	adress = models.CharField(max_length=20)
	complementadress = models.CharField(max_length=20)
	cep = models.CharField(max_length=20,null=True,blank=False)
	state = models.CharField(max_length=20, verbose_name='estado')
	country = CountryField()
	phone = models.CharField(max_length=20)
	celphone = models.CharField(max_length=20)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	update = models.DateTimeField(auto_now_add=False, auto_now=True)


	def __unicode__(self):
		return self.name

		