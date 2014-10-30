from django.shortcuts import render
from django.template.response import TemplateResponse
from django.conf import settings
# Create your views here.
def index(request):
    context = { 'active_tag': 'home', 'BASE_URL':settings.BASE_URL}
    return TemplateResponse(request, 'projects/index.html', context)
    
# from django.http import HttpResponse
# from django.template import RequestContext, loader
# from django.shortcuts import get_object_or_404, render
# from django.contrib.auth.forms import AuthenticationForm
# from django.template.response import TemplateResponse

# def index(request, template_name='home/index.html', authentication_form=AuthenticationForm,):
    #template = loader.get_template('home/index.html')
    # form = authentication_form(request)
    # context = {
        # 'form': form,
        # }
    #return render(request, 'home/index.html')
    # return TemplateResponse(request, template_name, context)