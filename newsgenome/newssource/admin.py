from newsgenome.newssource.models import Source, Entry
from django.contrib import admin

admin.site.register(Source)
admin.site.register(Entry)

class SourceAdmin(admin.ModelAdmin):
    pass
    
class EntryAdmin(admin.ModelAdmin):
    pass