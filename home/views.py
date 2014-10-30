from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.forms import AuthenticationForm
from django.template.response import TemplateResponse

def index(request, template_name='home/index.html', authentication_form=AuthenticationForm,):
    #template = loader.get_template('home/index.html')
    form = authentication_form(request)
    context = {
        'form': form,
        }
    #return render(request, 'home/index.html')
    return TemplateResponse(request, template_name, context)