from djangocalais.models import CalaisDocument

from django import template

register = template.Library()

@register.filter()
def select_calais_entities(value, entry):
	
	"Surrounds open calais entity detections with a special span tag that can be used to hook into JavaScript applications."
	calais_doc = CalaisDocument.objects.get_document_for_object(entry)
	
	for entity in calais_doc.entities.all():
		if(entity.type != 'URL'):
			value = value.replace(entity.name, '<span class="open-calais-entity">%s</span>' % ( entity.name ))
		
	return value
