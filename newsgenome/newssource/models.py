from datetime import datetime
from django.db import models
import django.contrib.auth.models as auth
from djangocalais.models import CalaisDocument

class Source(models.Model):
    title = models.CharField(max_length=200)
    rss_uri = models.URLField(verify_exists=True,verbose_name="News RSS Feed",null=False,blank=False)
    updated_by = models.ForeignKey(auth.User, related_name="source_updated_by")
    updated_at = models.DateTimeField(editable=True)

    def __unicode__(self):
        return unicode(self.title)

    def __str__(self):
        return self.title

class Entry(models.Model):
    source = models.ForeignKey(Source)
    title = models.CharField(max_length=200)
    entry_uri = models.URLField(verify_exists=True,verbose_name="News Entry URI",null=False,blank=False)
    content = models.TextField(blank=False)
    updated_by = models.ForeignKey(auth.User, related_name="entry_updated_by")
    updated_at = models.DateTimeField(editable=True)

    def __unicode__(self):
        return unicode(self.title)

    def __str__(self):
        return self.title

    def save(self):
        super(Entry, self).save()
        CalaisDocument.objects.analyze(self, fields=[('content', 'text/txt')])