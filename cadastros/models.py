from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Produto(models.Model):
	user = models.ForeignKey(User,related_name='produtos' ,null=True, blank=True)
	title = models.CharField(max_length=50)
	description = models.CharField(max_length=500, blank=True)
	price = models.DecimalField(max_digits=20, decimal_places=2,)


	def __unicode__(self):
		return self.title 