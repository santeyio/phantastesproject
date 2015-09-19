from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from models import Book, Day
from django.contrib.auth.decorators import login_required


@login_required(login_url='/account/login')
def index(request):
	readings = Book.objects.all()
	context = RequestContext(request, {
		'readings': readings,
	})
	return render(request, 'readings/index.html', context)

@login_required(login_url='/account/login')
def detail(request, reading_id):
	reading = get_object_or_404(Book, pk=reading_id)
	days = Day.objects.filter(book=reading_id)
	context = {'reading': reading, 'days': days}
	return render(request, 'readings/detail.html', context)
