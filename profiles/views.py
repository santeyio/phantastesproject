from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from models import Profile
from readings.models import Book, Day
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import datetime, operator, json

@login_required(login_url='/account/login')
def index(request, username):
    
    # logged in view
    if request.user.username == username:

        books = Book.objects.filter(active=True)
        all_books = Book.objects.all()
        book_dataset = []

        for book in all_books:
            # create list for smart search on books for quotes section
            book_dataset.append({'name': book.title + " (" + book.author + ")", 'id':  book.id})

        for book in books:
            timedelta =  datetime.date.today() - book.start_date 
            if timedelta.days < book.number_of_days:
                current_book = book
                days = Day.objects.filter(book=current_book)
                days = sorted(days, key=operator.attrgetter('day'), reverse=False)

        context = RequestContext(request, {
            'book': current_book,
            'day': days[timedelta.days],
            'book_dataset': json.dumps(book_dataset),
        })

        return render(request, 'profiles/index.html', context)

    # public view for users
    else:
        user = User.objects.get(username=username)
        return HttpResponse("yay! it worked! " + user.username)
