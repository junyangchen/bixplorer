from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url
from userprofile import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^(?P<user_id>\d+)/$', views.view_profile, name='view_profile'),     
    url(r'^$', views.view_profile, name='view_profile'), 
)