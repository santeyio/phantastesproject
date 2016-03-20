from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^voting/(?P<poll_id>[0-9]+)/$', views.voting, name='voting'),
	url(r'^nominations/(?P<poll_id>[0-9]+)/$', views.nominations, name='nominations'),
        url(r'^test_email_render/$', views.test_email_render, name='test_email_render'),
]
