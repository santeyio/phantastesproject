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
    user = User.objects.get(username=username)
    profile = Profile.objects.filter(user=user)
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


    # logged in view
    if request.user.username == username:
        context = RequestContext(request, {
            'book': current_book,
            'day': days[timedelta.days],
            'book_dataset': json.dumps(book_dataset),
            'profile': profile,
            'logged_in': True,
            'username': request.user.username,
        })

        return render(request, 'profiles/index.html', context)

    # public view for users
    else:
        context = RequestContext(request, {
            'book': current_book,
            'day': days[timedelta.days],
            'book_dataset': json.dumps(book_dataset),
            'profile': profile,
            'logged_in': False,
            'username': user.username,
        })
        return render(request, 'profiles/index.html', context)

def all(request):
    users = User.objects.all()
    users = sorted(users, key=operator.attrgetter('username'), reverse=False)
    posts_querydict = Post.objects.all().order_by('-id')
    posts = []
    for post in posts_querydict:
        posts.append({
            'id': post.id,
            'date': post.created.strftime('%d/%m/%Y %H:%M:%S'),
            'category': post.category,
            'book_title': post.book.title,
            'book_author': post.book.author,
            'title': post.title,
            'body': post.body,
            'user': post.user.username,
        })
    
    context = RequestContext(request, {
        'users': users,
        'posts': posts,
    })

    return render(request, 'profiles/all.html', context)

# ------------------
#   Ajax functions
# -----------------

def add_post(request):
    if request.method == "POST":
        content = request.POST['content']
        book = request.POST['book_id']
        category = request.POST['category']
        if category == 'thought':
            new_thought = Post(
                user = request.user,
                category = "thought",
                book = Book.objects.get(id=book),
                body = content
            )
            new_thought.save()
            return HttpResponse(True)
        elif category == 'underline':
            new_underline = Post(
                user = request.user,
                category = category,
                book = Book.objects.get(id=book),
                body = content
            )
            new_underline.save()
            return HttpResponse(True)
    else:
        return HttpResponse("Error")

def add_underline(request):
    if request.method == "POST":
        content = request.POST['underline_text']
        book = request.POST['book_id']
        new_thought = Post(
            user = request.user,
            category = "underline",
            book = Book.objects.get(id=book),
            body = content
        )
        new_thought.save()
        return HttpResponse(True)
    else:
        return HttpResponse("Error")

def get_user_feed(request):
    if request.method == "POST":
        username = request.POST['user']
        user = User.objects.get(username=username)
        posts_querydict = Post.objects.filter(user=user).order_by('-id')
        posts = []
        for post in posts_querydict:
            posts.append({
                'id': post.id,
                'date': post.created.strftime('%d/%m/%Y %H:%M:%S'),
                'category': post.category,
                'book_title': post.book.title,
                'book_author': post.book.author,
                'title': post.title,
                'body': post.body,
            })
        return HttpResponse(json.dumps(posts))
    else:
        return HttpResponse("Error")
