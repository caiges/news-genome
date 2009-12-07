from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from newsgenome.newssource.models import Source, Entry

def index(request):
	return render_to_response('main/index.html', {}, context_instance=RequestContext(request))
	
def list_sources(request):
	sources = Source.objects.all()
	return render_to_response('main/sources.html', {'sources' : sources}, context_instance=RequestContext(request))
	
def list_entries(request, source_id=None):
	source = Source.objects.get(id=source_id)
	entries = Entry.objects.all()
	return render_to_response('main/entries.html', {'source' : source, 'entries' : entries}, context_instance=RequestContext(request))
	
def show_entry(request, source_id=None, entry_id=None):
	source = Source.objects.get(id=source_id)
	entry = Entry.objects.get(id=entry_id)
	return render_to_response('main/entry.html', {'source' : source, 'entry' : entry}, context_instance=RequestContext(request))