from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'newsgenome.disambiguator.views.index'),
)