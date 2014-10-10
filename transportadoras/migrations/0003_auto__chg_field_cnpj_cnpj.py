# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Cnpj.cnpj'
        db.alter_column(u'transportadoras_cnpj', 'cnpj', self.gf('django.db.models.fields.CharField')(max_length=20))

    def backwards(self, orm):

        # Changing field 'Cnpj.cnpj'
        db.alter_column(u'transportadoras_cnpj', 'cnpj', self.gf('django.db.models.fields.IntegerField')(max_length=20))

    models = {
        u'transportadoras.cnpj': {
            'Meta': {'object_name': 'Cnpj'},
            'cnpj': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['transportadoras']