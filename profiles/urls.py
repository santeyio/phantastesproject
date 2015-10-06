from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^all/$', views.all, name='all'),
	url(r'^add_post/$', views.add_post, name='add_post'),
	url(r'^get_user_feed/$', views.get_user_feed, name='get_user_feed'),
	url(r'^(?P<username>.+)/$', views.index, name='index'),
]
