from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from django.http import HttpResponse
from readings.models import Book, Day
import datetime, operator

def index(request):
    books = Book.objects.filter(active=True)
    context = RequestContext(request,{})
    for book in books:
        timedelta = datetime.date.today() - book.start_date
        if timedelta.days < book.number_of_days:
            current_book = book
            days = Day.objects.filter(book=current_book)
            days = sorted(days, key=operator.attrgetter('day'), reverse=False)
            context = RequestContext(request, {
                'book': current_book,
                'day': days[timedelta.days],
            })
            break
        else:
            continue
    
    return render(request, 'homepage.html', context)

def about(request):
    context = RequestContext(request,{
    })
    return render(request, 'about.html', context)
