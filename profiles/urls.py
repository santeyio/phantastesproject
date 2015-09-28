from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^all/$', views.all, name='all'),
	url(r'^(?P<username>.+)/$', views.index, name='index'),
]
