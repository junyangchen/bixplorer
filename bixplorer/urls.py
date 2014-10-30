from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^$', include('home.urls', namespace="home")),
    url(r'^projects$', include('home.urls', namespace="home")),
)
