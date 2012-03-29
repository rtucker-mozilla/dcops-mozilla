# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'WorkLog'
        db.create_table(u'work_log', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('created_on', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('start_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('expected_completion_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('completion_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('assigned_to', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='assigned_to', null=True, to=orm['auth.User'])),
            ('priority', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['work_log.Priority'])),
            ('dc', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['work_log.DataCenter'])),
        ))
        db.send_create_signal('work_log', ['WorkLog'])

        # Adding model 'DataCenter'
        db.create_table('work_log_datacenter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('work_log', ['DataCenter'])

        # Adding model 'Priority'
        db.create_table(u'work_log_priority', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('work_log', ['Priority'])

        # Adding model 'Depends'
        db.create_table('work_log_depends', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('issue_id', self.gf('django.db.models.fields.IntegerField')()),
            ('direction', self.gf('django.db.models.fields.IntegerField')()),
            ('work_log', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['work_log.WorkLog'])),
        ))
        db.send_create_signal('work_log', ['Depends'])

        # Adding model 'Blocks'
        db.create_table('work_log_blocks', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('work_log', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['work_log.WorkLog'])),
        ))
        db.send_create_signal('work_log', ['Blocks'])


    def backwards(self, orm):
        
        # Deleting model 'WorkLog'
        db.delete_table(u'work_log')

        # Deleting model 'DataCenter'
        db.delete_table('work_log_datacenter')

        # Deleting model 'Priority'
        db.delete_table(u'work_log_priority')

        # Deleting model 'Depends'
        db.delete_table('work_log_depends')

        # Deleting model 'Blocks'
        db.delete_table('work_log_blocks')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'work_log.blocks': {
            'Meta': {'object_name': 'Blocks'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'work_log': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['work_log.WorkLog']"})
        },
        'work_log.datacenter': {
            'Meta': {'object_name': 'DataCenter'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'work_log.depends': {
            'Meta': {'object_name': 'Depends'},
            'direction': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue_id': ('django.db.models.fields.IntegerField', [], {}),
            'work_log': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['work_log.WorkLog']"})
        },
        'work_log.priority': {
            'Meta': {'object_name': 'Priority'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'work_log.worklog': {
            'Meta': {'object_name': 'WorkLog', 'db_table': "u'work_log'"},
            'assigned_to': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'assigned_to'", 'null': 'True', 'to': "orm['auth.User']"}),
            'completion_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'created_on': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dc': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['work_log.DataCenter']"}),
            'expected_completion_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'priority': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['work_log.Priority']"}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['work_log']
