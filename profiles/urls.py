from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^all/$', views.all, name='all'),
	url(r'^add_post/$', views.add_post, name='add_post'),
	url(r'^add_comment/$', views.add_comment, name='add_comment'),
	url(r'^get_user_feed/$', views.get_user_feed, name='get_user_feed'),
	url(r'^get_comments/$', views.get_comments, name='get_comments'),
	url(r'^post/(?P<post_id>[0-9]+)$', views.post_detail, name='post_detail'),
	url(r'^(?P<username>.+)/$', views.index, name='index'),
]
