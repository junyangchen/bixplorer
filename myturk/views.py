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
	context = 'The index method is called'
	return TemplateResponse(request, 'myturk/index.html', context)

# def createhit(request):
#     # Load dataset from database
#     datasets = DataSet.objects.all()    
#     context = { 'active_tag': 'myturk', 'BASE_URL':settings.BASE_URL, 'datasets':datasets}
#     return TemplateResponse(request, 'myturk/createhit.html', context)

def createhit(request):











	

	context = 'Called the createhit method'
	print('----------------------------')
	print(context)

	return TemplateResponse(request, 'myturk/createhit.html', context)




def createhitsubmit(request):

	context = 'Called the createhitSSSSubmit method'

	print('----------------------------')

	context.append(request.body)
	print(context)
	return HttpResponse(json.dumps(theresponse), content_type = "application/json")

	# return TemplateResponse(request, 'myturk/createhit.html', context)



