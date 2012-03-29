# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Depends'
        db.create_table('dcops_shipping_depends', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('issue_id', self.gf('django.db.models.fields.IntegerField')()),
            ('shipment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dcops_shipping.Shipment'])),
        ))
        db.send_create_signal('dcops_shipping', ['Depends'])


    def backwards(self, orm):
        
        # Deleting model 'Depends'
        db.delete_table('dcops_shipping_depends')


    models = {
        'dcops_shipping.depends': {
            'Meta': {'object_name': 'Depends'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue_id': ('django.db.models.fields.IntegerField', [], {}),
            'shipment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dcops_shipping.Shipment']"})
        },
        'dcops_shipping.shipment': {
            'Meta': {'object_name': 'Shipment'},
            'arrival_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'data_center': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'to': "orm['work_log.DataCenter']", 'null': 'True', 'blank': 'True'}),
            'delivered': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
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
        },
        'work_log.datacenter': {
            'Meta': {'object_name': 'DataCenter'},
            'color': ('django.db.models.fields.CharField', [], {'default': "'blue'", 'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['dcops_shipping']
