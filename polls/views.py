from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return HttpResponse("Hey! You made it to the polls page.")
