from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url
from projects import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^createhit/$', views.createhit, name='createhit'),
)