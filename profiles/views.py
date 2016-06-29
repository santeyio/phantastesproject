from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from models import Profile, Post, PostComment
from forms import ProfileForm
from readings.models import Book, Day
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import datetime, operator, json

@login_required(login_url='/account/login')
def index(request, username):

    # set context dict
    context_dict = {}

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

    context_dict['book_dataset'] = json.dumps(book_dataset)

    for book in books:
        timedelta =  datetime.date.today() - book.start_date 
        if timedelta.days < book.number_of_days:
            days = Day.objects.filter(book=book)
            days = sorted(days, key=operator.attrgetter('day'), reverse=False)
            context_dict['day'] = days[timedelta.days]
            context_dict['book'] = book

    context_dict['profile'] = profile

    # logged in view
    if request.user.username == username:
        context_dict['logged_in'] = True
        context_dict['username'] = request.user.username

    # public view for users
    else:
        context_dict['logged_in'] = False
        context_dict['username'] = user.username

    context = RequestContext(request, context_dict)
    return render(request, 'profiles/index.html', context)

@login_required(login_url='/account/login')
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

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    
    context = RequestContext(request, {
        'post': post,
    })

    return render(request, 'profiles/post_detail.html', context)

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

def get_comments(request):
    if request.method == "POST":
        post_id = request.POST['post_id']
        post = Post.objects.get(id=post_id)
        comments_querydict = PostComment.objects.filter(post=post).order_by('-created')
        comments = []
        for comment in comments_querydict:
            comments.append({
                'id': comment.id,
                'date': comment.created.strftime('%d/%m/%Y %H:%M:%S'),
                'user': comment.user.username,
				'comment': comment.comment
            })
        return HttpResponse(json.dumps(comments))
    else:
        return HttpResponse("Error")

def add_comment(request):
    if request.method == "POST":
        comment = request.POST['comment']
        post = request.POST['post_id']
        new_comment = PostComment(
            user = request.user,
            post = Post.objects.get(id=post),
            comment = comment,
        )
        #return HttpResponse(json.dumps(post))
        new_comment.save()
        return HttpResponse(True)
    else:
        return HttpResponse("Error")
