# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Shipper'
        db.create_table('dcops_shipping_shipper', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('dcops_shipping', ['Shipper'])

        # Adding model 'Shipment'
        db.create_table('dcops_shipping_shipment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('shipper', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dcops_shipping.Shipper'])),
            ('signed_for_by', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('tracking_number', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('ship_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('arrival_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('dcops_shipping', ['Shipment'])


    def backwards(self, orm):
        
        # Deleting model 'Shipper'
        db.delete_table('dcops_shipping_shipper')

        # Deleting model 'Shipment'
        db.delete_table('dcops_shipping_shipment')


    models = {
        'dcops_shipping.shipment': {
            'Meta': {'object_name': 'Shipment'},
            'arrival_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'ship_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'shipper': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dcops_shipping.Shipper']"}),
            'signed_for_by': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tracking_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'dcops_shipping.shipper': {
            'Meta': {'object_name': 'Shipper'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['dcops_shipping']
