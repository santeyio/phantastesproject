from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from models import Poll, Book, Vote
from forms import BookForm
from django.contrib.auth.models import User
import datetime, pytz, operator


@login_required(login_url='/account/login')
def index(request):
    polls = Poll.objects.filter()
    today = datetime.datetime.now(tz=pytz.utc)
    ztime = datetime.timedelta(days=0)

    nomination_open_poll = None
    voting_poll = None

    for poll in polls:
        timedelta_nomination = poll.nominations_open - today
        timedelta_voting_open = poll.voting_open - today
        timedelta_voting_close = poll.voting_close - today

        # open nomination polls
        if timedelta_nomination <= ztime and timedelta_voting_open >= ztime:
            nomination_open_poll = poll

        # open voting polls
        if timedelta_voting_open <= ztime and timedelta_voting_close >= ztime:
            voting_poll = poll
        
    context = RequestContext(request, {
            'nomination_poll': nomination_open_poll,
            'voting_poll': voting_poll,
    })
    return render(request, 'polls/index.html', context)

@login_required(login_url='/account/login')
def voting(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    books = Book.objects.filter(poll=poll_id)
    already_voted = Vote.objects.filter(user=request.user).filter(poll=poll)
    
    for book in books:
        number_of_votes = Vote.objects.filter(book=book)
        book.votes = len(number_of_votes)

    books = sorted(books, key=operator.attrgetter('votes'), reverse=True)

    if len(already_voted) >= 3:
        disabled = 'disabled="disabled"'
    else:
        disabled = ''


    context = RequestContext(request, {
        'poll': poll,
        'books': books,
        'disabled': disabled,
        'already_voted': len(already_voted),
    })

    if request.method == "POST":
        for book in books:
            votes = request.REQUEST[str(book.id)]
            if votes:
                i = int(votes)
                while i > 0:
                    vote = Vote(user=request.user, poll=poll, book=book)
                    vote.save()
                    i -= 1
                    # return HttpResponse(i)
            else:
                continue
        return redirect('/polls/voting/' + str(poll_id))
        
    return render(request, 'polls/voting.html', context)

@login_required(login_url='/account/login')
def nominations(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    books = Book.objects.filter(poll=poll_id)
    disabled = ''
    votes = {}

    for book in books:
        if book.user == request.user:
            disabled = 'disabled="disabled"'

    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            description = form.cleaned_data['description']
            book = Book(title=title, author=author, description=description, poll=poll, user=request.user)
            book.save()
            return redirect('/polls/nominations/' + str(poll_id))
    else:
        form = BookForm()

    context = RequestContext(request, {
        'poll': poll,
        'books': books,
        'form': form,
        'disabled': disabled,
    })
    return render(request, 'polls/nominations.html', context)
