from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from phantastes import views

from django.contrib import admin


urlpatterns = patterns(
    "",
    url(r"^$", views.index, name="home"),
    url(r"^forum/", include('spirit.urls')),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
    url(r"^profile/", include("profiles.urls", namespace="profiles")),
    url(r"^polls/", include("polls.urls", namespace="polls")),
    url(r"^readings/", include("readings.urls", namespace="readings")),
    url(r"^about/$", views.about, name="about"),
    url(r'^chat/', include('djangoChat.urls')),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
