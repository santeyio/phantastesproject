from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Schedule, Day


def index(request):
	readings = Schedule.objects.all()
	template = loader.get_template('readings/index.html')
	context = RequestContext(request, {
		'readings': readings,
	})
	return HttpResponse(template.render(context))

