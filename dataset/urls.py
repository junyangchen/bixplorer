from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url
from dataset import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^test/$', views.load_docs_by_datasetId, name='test'),   
)