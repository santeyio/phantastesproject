from django.db import models

class Poll(models.Model):
	title 				= models.CharField(max_length=200)
	notes 				= models.TextField(blank=True, null=True)
	nominations_open	= models.DateTimeField('date voting beings')
	voting_open 		= models.DateTimeField('date voting beings')
	voting_close 		= models.DateTimeField('date voting closes')
	pub_date 			= models.DateTimeField('date created')

	def __str__(self):
		return self.title
	

class Book(models.Model):
	poll 				= models.ForeignKey(Poll)
	title 				= models.CharField(max_length=200)
	author 				= models.CharField(max_length=200)
	description 		= models.TextField()

	def __str__(self):
		return self.title
