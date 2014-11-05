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

@login_required
def view_profile(request, **kwargs):
    '''
    Display a user's profile. If user_id if provided, then the user 
    will be the user of the user id. Otherwise, the user will be the
    login user.
    '''
    
    if 'user_id' in kwargs:
        user_id = kwargs['user_id']
        thisuser = User.objects.get(pk = user_id)
    else:
        thisuser = request.user
        
    try:        
        from django.contrib.admin.models import LogEntry
        
        new_logging_list = []
        # Dispay the logActions only when "this user" is the loggin user. 
        if thisuser == request.user:
            hist_actions = LogEntry.objects.filter(user = request.user)
            actions_list = list(hist_actions)           
            action_dict = { '1' : "add", '2' : 'update', '3' : 'delete'}
            
            # rebuild the logging list
            for item in actions_list:
                logContentType = item.content_type 
                logAction = item.action_flag
                logObject = None
                targetObject = None
                
                try:    
                    logObject = logContentType.get_object_for_this_type(pk=item.object_id)
                except Exception as e:
                    logObject = None                
                
                logAction = action_dict[str(logAction)]
                
                new_logging_list.append({'action_time':item.action_time, 
                    'change_message':item.change_message, 
                    'logObject':logObject, 
                    'logAction' : logAction,
                    'logContentType': logContentType.name})

        profile = thisuser.userprofile    
        context = { "profile":profile, "this_user":thisuser, 'active_tag': 'userprofile', 
            'BASE_URL':settings.BASE_URL, 'history_actions': new_logging_list}
        return TemplateResponse(request, 'userprofile/view_profile.html', context) 
    except Exception as e:
        return HttpResponse(e)    