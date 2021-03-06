# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CPFCNPJModel'
        db.create_table(u'transportadoras_cpfcnpjmodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'transportadoras', ['CPFCNPJModel'])


    def backwards(self, orm):
        # Deleting model 'CPFCNPJModel'
        db.delete_table(u'transportadoras_cpfcnpjmodel')


    models = {
        u'transportadoras.cpfcnpjmodel': {
            'Meta': {'object_name': 'CPFCNPJModel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['transportadoras']