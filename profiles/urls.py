from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^all/$', views.all, name='all'),
	url(r'^add_thought/$', views.add_thought, name='add_thought'),
	url(r'^(?P<username>.+)/$', views.index, name='index'),
]
