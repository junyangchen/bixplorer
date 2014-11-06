from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.http import HttpResponseNotAllowed, HttpResponseForbidden, Http404
from django.conf import settings
from itertools import chain
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.models import User
from projects.models import DataSet
import json
from home.utils import * 



def index(request):
	context = 'Test the response to index page'
	return TemplateResponse(request, 'myturk/index.html', context)

def createhit(request):
    # Load dataset from database
    datasets = DataSet.objects.all()    
    context = { 'active_tag': 'myturk', 'BASE_URL':settings.BASE_URL, 'datasets':datasets}
    return TemplateResponse(request, 'myturk/createhit.html', context)

def testcreatehit(request):
	context = 'Test the response to createhit page'
	return TemplateResponse(request, 'myturk/createhit.html', context)


