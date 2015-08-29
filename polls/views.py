from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required


@login_required(login_url='/account/login')
def index(request):
	readings = {}
	context = RequestContext(request, {
		'readings': readings,
	})
	return render(request, 'polls/index.html', context)
