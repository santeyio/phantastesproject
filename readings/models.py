from django.db import models

class Schedule(models.Model):
	title 				= models.CharField(max_length=200)
	description			= models.TextField()

	def __str__(self):
		return self.title

class Day(models.Model):
	schedule			= models.ForeignKey(Schedule)
	date				= models.DateField()
	reading				= models.CharField(max_length=400)
	description			= models.CharField(max_length=500, blank=True, null=True)
