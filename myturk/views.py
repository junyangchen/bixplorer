from django.shortcuts import render

# Create your views here.

def index(request):
    context = 'Test the response to index page'
    return TemplateResponse(request, 'projects/index.html', context)


def createhit():
	context = 'Test the response to createhit page'
    return TemplateResponse(context)

