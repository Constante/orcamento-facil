 #!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Orcamento(models.Model):
	NACIONALIDADE= (
		('Brasileiro', 'Brasileiro'),
		('Alemão', 'Bugre'),
	)
	nacionalidade=models.CharField(max_length=1, choices=NACIONALIDADE)
	produto=models.CharField(max_length=120) 
	quantidade=models.IntegerField()
	valor=models.DecimalField(max_length=120,max_digits=100,decimal_places=2, null=False, blank=False,default=0.00)
    

	def __unicode__(self):
		return self.produto


