from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from models import Profile, Post
from forms import ProfileForm
from readings.models import Book, Day
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import datetime, operator, json

@login_required(login_url='/account/login')
def index(request, username):

    # check if profile exists 
    profile = Profile.objects.filter(user=request.user)
    if not profile:
        profile = False
    else:
        profile = profile[0]
    

    # upload profile pic
    if request.method == "POST":
        if profile:
            profile(avatar=request.FILES['avatar'])
            profile.save()
        else:
            profile = Profile(user=request.user, avatar=request.FILES['avatar'])
            profile.save()

    # logged in view
    if request.user.username == username:

        books = Book.objects.filter(active=True)
        all_books = Book.objects.all()
        book_dataset = {}


        for book in all_books:
            # create list for smart search on books for quotes section
            book_dataset[book.title + " - " + book.author] = book.id

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
            'logged_in': True,
            'profile': profile,
        })

        return render(request, 'profiles/index.html', context)

    # public view for users
    else:
        user = User.objects.get(username=username)
        context = RequestContext(request, {
            'logged_in': False,
        })
        return render(request, 'profiles/index.html', context)

def all(request):
    users = User.objects.all()
    users = sorted(users, key=operator.attrgetter('username'), reverse=False)
    
    context = RequestContext(request, {
        'users': users,
    })

    return render(request, 'profiles/all.html', context)

# ------------------
#   Ajax functions
# -----------------

def add_thought(request):
    if request.method == "POST":
        content = request.POST['thought_text']
        book = request.POST['book_id']
        new_thought = Post(
            user = request.user,
            category = "thought",
            book = Book.objects.get(id=book),
            body = content
        )
        new_thought.save()
        return HttpResponse(True)
    else:
        return HttpResponse("Error")

def add_underline(request):
    if request.method == "POST":
        pass
    else:
        return HttpResponse("Error")

def get_user_feed(request):
    if request.method == "POST":
        username = request.POST['user']
        user = User.objects.get(username=username)
        posts = Post.objects.find(user=user)
    else:
        return HttpResponse("Error")
