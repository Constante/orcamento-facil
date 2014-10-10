 #!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class Cnpj(models.Model):
    user = models.ForeignKey(User,unique=True,null=True,blank=True)
    nome = models.CharField(max_length=120,null=True,blank=False)
    cnpj = models.CharField(max_length=20,null=False,blank=False)
    

    def __unicode__(self):
    	return unicode(self.nome)