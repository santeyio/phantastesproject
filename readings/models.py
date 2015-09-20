from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title 		= models.CharField(max_length=200)
    author		= models.CharField(max_length=200)
    description		= models.TextField()
    start_date		= models.DateField()
    number_of_days	= models.IntegerField()
    active		= models.BooleanField()

    def __str__(self):
        return self.title

class Day(models.Model):
    book		= models.ForeignKey(Book)
    day			= models.IntegerField()
    reading		= models.CharField(max_length=400)
    description		= models.CharField(max_length=500, blank=True, null=True)

