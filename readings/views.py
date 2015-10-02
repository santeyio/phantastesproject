from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from models import Book, Day
from django.contrib.auth.decorators import login_required
import operator


def index(request):
	readings = Book.objects.all()
	context = RequestContext(request, {
		'readings': readings,
	})
	return render(request, 'readings/index.html', context)

def detail(request, reading_id):
    reading = get_object_or_404(Book, pk=reading_id)
    days = Day.objects.filter(book=reading_id)

    days = sorted(days, key=operator.attrgetter('day'), reverse=False)
    context = RequestContext(request, {
        'reading': reading, 
        'days': days,
    })
    return render(request, 'readings/detail.html', context)
