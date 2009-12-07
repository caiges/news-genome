from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'newsgenome.main.views.index'),
	(r'sources/$', 'newsgenome.main.views.list_sources'),
	(r'sources/(?P<source_id>\d+)/entries/$', 'newsgenome.main.views.list_entries'),
	(r'sources/(?P<source_id>\d+)/entries/(?P<entry_id>\d+)/$', 'newsgenome.main.views.show_entry'),
)