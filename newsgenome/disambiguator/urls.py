from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns('newsgenome.disambiguator.views',
    url(r'^search/(?P<search_excerpt>.+)$', 'disambiguate',name='disambiguate_excerpt'),
)