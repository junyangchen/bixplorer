from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render

def index(request):
    #template = loader.get_template('home/index.html')
    return render(request, 'home/index.html')