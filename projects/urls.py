from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url
from projects import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^(?P<project_id>\d+)/$', views.detail, name='detail'),
    url(r'^add/$', views.add, name='add'),
    url(r'^plist/$', views.plist, name='plist'),
    url(r'^edit/(?P<project_id>\d+)/$', views.edit, name='edit'),
    url(r'^delete/(?P<project_id>\d+)/$', views.delete, name='delete'),
    url(r'^(?P<project_id>\d+)/comment/add/$', views.add_comment, name='add_comment'),
    #url(r'^(?P<project_id>\d+)/comment/$', views.comment, name='comment'),
    url(r'^comment/delete/$', views.delete_comment, name='delete_comment'), 
    url(r'^collaborator/add/$', views.add_collaborator, name='add_collaborator'), 
    url(r'^collaborator/delete/$', views.delete_collaborator, name='delete_collaborator'), 
    url(r'^test/$', views.load_project_comment_json, name='test'),   
)