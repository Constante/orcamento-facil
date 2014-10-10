# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Orcamento'
        db.create_table(u'orcamentos_orcamento', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('produto', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('quantidade', self.gf('django.db.models.fields.IntegerField')()),
            ('valor', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_length=120, max_digits=100, decimal_places=2)),
        ))
        db.send_create_signal(u'orcamentos', ['Orcamento'])


    def backwards(self, orm):
        # Deleting model 'Orcamento'
        db.delete_table(u'orcamentos_orcamento')


    models = {
        u'orcamentos.orcamento': {
            'Meta': {'object_name': 'Orcamento'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'produto': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'quantidade': ('django.db.models.fields.IntegerField', [], {}),
            'valor': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_length': '120', 'max_digits': '100', 'decimal_places': '2'})
        }
    }

    complete_apps = ['orcamentos']