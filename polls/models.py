from django.db import models
from django.contrib.auth.models import User


class Poll(models.Model):
    title               = models.CharField(max_length=200)
    notes               = models.TextField(blank=True, null=True)
    nominations_open    = models.DateTimeField('Date nominations open')
    voting_open         = models.DateTimeField('Date voting begins')
    voting_close        = models.DateTimeField('Date voting closes')
    pub_date            = models.DateTimeField('Date created')

    def __str__(self):
        return self.title
        

class Book(models.Model):
    poll                = models.ForeignKey(Poll)
    title               = models.CharField(max_length=200)
    author              = models.CharField(max_length=200)
    description         = models.TextField()
    user                = models.ForeignKey(User)

    def __str__(self):
        return self.title

class Vote(models.Model):
    poll                = models.ForeignKey(Poll)
    book                = models.ForeignKey(Book)
    user                = models.ForeignKey(User)
