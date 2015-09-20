from django.db import models
from django.contrib.auth.models import User
from readings.models import Book

class Profile(models.Model):
	user = models.OneToOneField(User)
	avatar = models.ImageField()
	status = models.CharField(blank=True, null=True, max_length=500)

class Quote(models.Model):
    book		= models.ForeignKey(Book)
    user 		= models.OneToOneField(User)
    quote		= models.TextField()

class Post(models.Model):
    user        = models.ForeignKey(User)
    title       = models.CharField(max_length=200)
    post        = models.TextField()
