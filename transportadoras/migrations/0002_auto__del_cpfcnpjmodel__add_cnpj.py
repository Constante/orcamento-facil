# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'CPFCNPJModel'
        db.delete_table(u'transportadoras_cpfcnpjmodel')

        # Adding model 'Cnpj'
        db.create_table(u'transportadoras_cnpj', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cnpj', self.gf('django.db.models.fields.IntegerField')(max_length=20)),
        ))
        db.send_create_signal(u'transportadoras', ['Cnpj'])


    def backwards(self, orm):
        # Adding model 'CPFCNPJModel'
        db.create_table(u'transportadoras_cpfcnpjmodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'transportadoras', ['CPFCNPJModel'])

        # Deleting model 'Cnpj'
        db.delete_table(u'transportadoras_cnpj')


    models = {
        u'transportadoras.cnpj': {
            'Meta': {'object_name': 'Cnpj'},
            'cnpj': ('django.db.models.fields.IntegerField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['transportadoras']