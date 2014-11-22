from django.shortcuts import render

from django.http import HttpResponse

import csv, json
import wikipedia

# import wikisettings


# Create your views here.

def org(request):

	org = "FBI"

	try:
		orginfo = wikipedia.summary(org)
	except wikipedia.exceptions.DisambiguationError as e:
		options = e.options

		return HttpResponse(options) 


	orginfo = wikipedia.summary(org)

	return HttpResponse(orginfo) 




def wikilocation(request):

		
	try:
		mercury = wikipedia.summary("blacksburg")
	except wikipedia.exceptions.DisambiguationError as e:
		options = e.options

		return HttpResponse(options) 


	result = []
	result.append (wikipedia.summary("blacksburg"))

	return HttpResponse(result) 

