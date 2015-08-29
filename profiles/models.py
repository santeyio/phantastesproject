from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User)
	avatar = models.ImageField()
	status = models.CharField(blank=True, null=True, max_length=500)
