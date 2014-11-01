# Django
from django.http import HttpResponse
from django.shortcuts import render_to_response #render
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from userprofile.models import UserProfile
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.conf import settings
from django.template.response import TemplateResponse

@login_required
def view_profile(request):    
    #if request.user.is_authenticated():
    #    uname = request.user.username
    thisuser = request.user
    try:
        profile = thisuser.userprofile    
        context = { "profile":profile, "user":thisuser, 'active_tag': 'userprofile', 'BASE_URL':settings.BASE_URL}
        return TemplateResponse(request, 'userprofile/view_profile.html', context) 
    except:    
        #profile = thisuser.userprofile
        return HttpResponse('Something is wrong')
