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
from types import *

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
    # uname = request.user.username
    thisuser = request.user    
    try:
        #hist_actions = user_history_actions(request)
        from django.contrib.admin.models import LogEntry
      
        hist_actions = LogEntry.objects.filter(user = request.user)
        actions_list = list(hist_actions)
        
        temp = ''
        newList = []
        action_dict = { '1' : "add", '2' : 'update', '3' : 'delete'}
        # rebuild the logEntry
        for item in actions_list:
            newItem = []
            logContentType = item.content_type 
            logAction = item.action_flag
            logObject = None
            targetObject = None
            
            try:    
                logObject = logContentType.get_object_for_this_type(pk=item.object_id)
            except Exception as e:
                logObject = None    
            
            print logContentType.name
            print logObject
            logAction = action_dict[str(logAction)]            
            
            newList.append({'action_time':item.action_time, 
                'change_message':item.change_message, 
                'logObject':logObject, 
                'logAction' : logAction,
                'logContentType': logContentType.name})
            
        profile = thisuser.userprofile    
        context = { "profile":profile, "user":thisuser, 'active_tag': 'userprofile', 'BASE_URL':settings.BASE_URL, 'history_actions': newList}
        return TemplateResponse(request, 'userprofile/view_profile.html', context) 
    except Exception as e:    
        #profile = thisuser.userprofile
        return HttpResponse(e)

# List recent actions for the user       