from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from models import Profile
from django.contrib.auth.decorators import login_required

@login_required(login_url='/account/login')
def index(request, username):
	#readings = Schedule.objects.all()
	#context = RequestContext(request, {
	#	'readings': readings,
	#})
	context = RequestContext(request, {
	})
	return render(request, 'profiles/index.html', context)
