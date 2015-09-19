from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from models import Profile
from readings.models import Book, Day
from django.contrib.auth.decorators import login_required
import datetime

@login_required(login_url='/account/login')
def index(request, username):
	books = Book.objects.filter(active=True)
	for book in books:
		timedelta = datetime.date.today() - book.start_date
		if timedelta.days < book.number_of_days:
			current_book = book
			days = Day.objects.filter(book=current_book)
			break
		else:
			continue

	context = RequestContext(request, {
		'book': current_book,
		'day': days[timedelta.days],
	})

	return render(request, 'profiles/index.html', context)
