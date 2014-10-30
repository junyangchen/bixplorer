# Django
from django.http import HttpResponse
from django.shortcuts import render_to_response #render
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from userprofile.models import UserProfile
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

@login_required
def view_profile(request):    
    if request.user.is_authenticated():
        uname = request.user.username
    thisuser = User.objects.get(username = uname)
    print thisuser.email
    
    try:
        profile = thisuser.userprofile
        context         = RequestContext(request, {"profile":profile, "user":thisuser})
        # return render_to_response("userprofile/view_profile.html", context)
        return render_to_response("userprofile/view_profile.html", context)
    except:    
        #profile = thisuser.userprofile
        return render_to_response("userprofile/view_profile.html", {"user":thisuser})
