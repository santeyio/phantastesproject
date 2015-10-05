from django.db import models
from django.contrib.auth.models import User
from readings.models import Book

class Profile(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(blank=True, null=True)
    status = models.CharField(blank=True, null=True, max_length=500)

class Post(models.Model):
    user        = models.ForeignKey(User)
    category    = models.CharField(max_length=20)
    title       = models.CharField(max_length=200, blank=True, null=True)
    book	= models.ForeignKey(Book, blank=True, null=True)
    body        = models.TextField(blank=True, null=True)

class PostComment(models.Model):
    user        = models.ForeignKey(User)
    post        = models.ForeignKey(Post)
    comment     = models.TextField()

class PostLike(models.Model):
    user        = models.ForeignKey(User)
    post        = models.ForeignKey(Post)
