from django.shortcuts import render

def index(request):
	context = 'Test the response to index page'
	return TemplateResponse(request, 'projects/index.html', context)

def createhit(request):
	context = 'Test the response to createhit page'
	return TemplateResponse(context)

