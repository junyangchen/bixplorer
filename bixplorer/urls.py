from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace="polls")),
	url(r'^$', include('home.urls', namespace="home")),
    url(r'^admin/', include(admin.site.urls)),
	#(r'^accounts/', include('registration.backends.default.urls')),
	(r'^accounts/', include('registration2.backends.simple.urls')),   
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
