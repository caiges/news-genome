from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def index(request):
	return render_to_response('disambiguator/index.html')