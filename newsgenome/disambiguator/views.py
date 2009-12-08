from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

import django.utils.simplejson as json
from httplib import HTTPConnection 


def disambiguate(request,search_excerpt='news+genome'):
    excerpt = search_excerpt
    search_url = '/sparql?default-graph-uri=http%3A%2F%2Fdbpedia.org&should-sponge=&query=SELECT++DISTINCT+%3Fs1+AS+%3Fc1%2C%0D%0A+++++++++++%28+bif%3Asearch_excerpt+%0D%0A+++++++++++++%28+bif%3Avector+%0D%0A+++++++++++++++%28+%27'+excerpt+'%27+%29%2C+%0D%0A+++++++++++++++%3Fo1%0D%0A+++++++++++++%29%0D%0A+++++++++++%29+AS+%3Fc2%2C+%0D%0A+++++++++++%3Fsc%2C+%0D%0A+++++++++++%3Frank+%0D%0A+++++WHERE+%7B%0D%0A+++++++++++++%7B%7B+SELECT++%3Fs1%2C+%0D%0A++++++++++++++++++++++++%28%3Fsc+*+3e-1%29+AS+%3Fsc%2C+%0D%0A++++++++++++++++++++++++%3Fo1%2C+%0D%0A++++++++++++++++++++++++%28sql%3Arnk_scale+%28%3CLONG%3A%3AIRI_RANK%3E+%28%3Fs1%29%29%29+AS+%3Frank++%0D%0A++++++++++++++++++WHERE+%7B+%3Fs1++%3Fs1textp++++++%3Fo1+++++++++++++++++++++++++++++.+%0D%0A++++++++++++++++++++++++++%3Fo1++bif%3Acontains++%27%22'+excerpt+'%22%27++%0D%0A+++++++++++++++++++++++++++++++OPTION+%28score+%3Fsc%29+%0D%0A++++++++++++++++++++++++%7D%0D%0A++++++++++++++++++ORDER+BY++DESC+%28%3Fsc+*+3e-1+%2B+sql%3Arnk_scale+%28%3CLONG%3A%3AIRI_RANK%3E+%28%3Fs1%29%29%29++%0D%0A++++++++++++++++++LIMIT+++++7%0D%0A++++++++++++++++++OFFSET++++0+%0D%0A++++++++++++++%7D%7D%0D%0A++++++++++++%7D&format=application%2Fsparql-results%2Bjson&debug=on&timeout='
    
    conn = HTTPConnection('dbpedia.org', 80)
    conn.request('GET',search_url)
    js = conn.getresponse().read() 

    js_object = json.loads(js)

    entries = [] 
    for item in js_object['results']['bindings']:
        entries.append(item)
    
    return 	HttpResponse(json.JSONEncoder().encode(js_object['results']['bindings']), mimetype='application/json')
	
