from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url
from wiki import views

urlpatterns = patterns('',
						# url(r'^$', views.index, name='index'),
                        url(r'^wikilocation/$', views.wikilocation, name='wikilocation'),
                        url(r'^org/$', views.org, name='org'),

                        )