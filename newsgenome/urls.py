
from django.conf.urls.defaults import patterns, include, handler500,url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

handler500 # Pyflakes

urlpatterns = patterns(
    '',
	url(r'^$', 'newsgenome.views.index'),
    (r'^admin/(.*)', admin.site.root),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
		(r'^disambiguator/', include( 'newsgenome.disambiguator.urls' )),
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
