from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url
from myturk import views

urlpatterns = patterns('',
                        url(r'^$', views.index, name='index'),
                        url(r'^createhit/$', views.createhit, name='createhit'),
                        )