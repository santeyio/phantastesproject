from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from models import Schedule, Day


def index(request):
	readings = Schedule.objects.all()
	context = RequestContext(request, {
		'readings': readings,
	})
	return render(request, 'readings/index.html', context)

def detail(request, reading_id):
	reading = get_object_or_404(Schedule, pk=reading_id)
	days = Day.objects.filter(schedule=reading_id)
	context = {'reading': reading, 'days': days}
	return render(request, 'readings/detail.html', context)
