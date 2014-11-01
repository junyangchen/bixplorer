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
from home.utils import * 

def log_addition(self, request, object):
    """
    Log that an object has been successfully added.
    The default implementation creates an admin LogEntry object.
    """
    from django.contrib.admin.models import LogEntry, ADDITION
    LogEntry.objects.log_action(
        user_id=request.user.pk,
        content_type_id=get_content_type_for_model(object).pk,
        object_id=object.pk,
        object_repr=force_text(object),
        action_flag=ADDITION
    )

@login_required
def view_profile(request):    
    #if request.user.is_authenticated():
    #    uname = request.user.username
    thisuser = request.user
    try:
        #hist_actions = user_history_actions(request)
        from django.contrib.admin.models import LogEntry
        data = LogEntry.objects.all() #.select_related('user', 'content_type').only('content_type', 'user')[:]

        users = lambda data: list(set([(d.user_id, d.user.get_full_name() if d.user.get_full_name() else d.user.username) \
                                       for d in data]))
        content_types = lambda data: list(set([(d.content_type_id, d.content_type.name) for d in data]))
        
        hist_actions = LogEntry.objects.filter(user = request.user)
        choices=users(data)
        temp = ''
        for item in hist_actions:
            contentType = item.content_type
            temp = temp + str(item.content_type.get_object_for_this_type(pk=item.object_id)) + " SEP "
        
        #return HttpResponse(str(temp))
        profile = thisuser.userprofile    
        context = { "profile":profile, "user":thisuser, 'active_tag': 'userprofile', 'BASE_URL':settings.BASE_URL, 'history_actions': hist_actions}
        return TemplateResponse(request, 'userprofile/view_profile.html', context) 
    except Exception as e:    
        #profile = thisuser.userprofile
        return HttpResponse(e)

# List recent actions for the user       