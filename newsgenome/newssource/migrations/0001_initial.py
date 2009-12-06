
from south.db import db
from django.db import models
from newsgenome.newssource.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Entry'
        db.create_table('newssource_entry', (
            ('id', models.AutoField(primary_key=True)),
            ('source', models.ForeignKey(orm.Source)),
            ('title', models.CharField(max_length=200)),
            ('entry_uri', models.URLField(blank=False, null=False, verify_exists=True)),
            ('content', models.TextField(blank=False)),
            ('updated_by', models.ForeignKey(orm['auth.User'], related_name="entry_updated_by")),
            ('updated_at', models.DateTimeField(editable=False)),
        ))
        db.send_create_signal('newssource', ['Entry'])
        
        # Adding model 'Source'
        db.create_table('newssource_source', (
            ('id', models.AutoField(primary_key=True)),
            ('title', models.CharField(max_length=200)),
            ('rss_uri', models.URLField(blank=False, null=False, verify_exists=True)),
            ('updated_by', models.ForeignKey(orm['auth.User'], related_name="source_updated_by")),
            ('updated_at', models.DateTimeField(editable=False)),
        ))
        db.send_create_signal('newssource', ['Source'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Entry'
        db.delete_table('newssource_entry')
        
        # Deleting model 'Source'
        db.delete_table('newssource_source')
        
    
    
    models = {
        'newssource.entry': {
            'content': ('models.TextField', [], {'blank': 'False'}),
            'entry_uri': ('models.URLField', [], {'blank': 'False', 'null': 'False', 'verify_exists': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'source': ('models.ForeignKey', ["orm['newssource.Source']"], {}),
            'title': ('models.CharField', [], {'max_length': '200'}),
            'updated_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'updated_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"entry_updated_by"'})
        },
        'auth.user': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'newssource.source': {
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'rss_uri': ('models.URLField', [], {'blank': 'False', 'null': 'False', 'verify_exists': 'True'}),
            'title': ('models.CharField', [], {'max_length': '200'}),
            'updated_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'updated_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"source_updated_by"'})
        }
    }
    
    complete_apps = ['newssource']
