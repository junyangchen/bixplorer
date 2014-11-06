from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.http import HttpResponseNotAllowed, HttpResponseForbidden, Http404
from django.conf import settings
from itertools import chain
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.models import User
from projects.models import DataSet
from dataset.models import Doc
import json
from home.utils import * 



def index(request):
	context = 'The index method is called'
	return TemplateResponse(request, 'myturk/index.html', context)

# def createhit(request):
#     # Load dataset from database
#     datasets = DataSet.objects.all()    
#     context = { 'active_tag': 'myturk', 'BASE_URL':settings.BASE_URL, 'datasets':datasets}
#     return TemplateResponse(request, 'myturk/createhit.html', context)

def createhit(request):
    datasets = DataSet.objects.all()   
    context = { 'active_tag': 'myturk', 'BASE_URL':settings.BASE_URL, 'datasets':datasets}	
    return TemplateResponse(request, 'myturk/createhit.html', context)
    
    
def createhitsubmit(request):
    from boto.mturk.connection import MTurkConnection
    from boto.mturk.question import QuestionContent,Question,QuestionForm,Overview,AnswerSpecification,SelectionAnswer,FormattedContent,FreeTextAnswer
    import connectMturk as mtconnection
    print 'Ok'
    # Get request data from the front-end
    requestJson = json.loads(request.body)    
    
    user_aws_secret_key = requestJson['aws_secret_key']    
    user_aws_access_key_id = requestJson['aws_access_key_id']
    task_selected_docs = requestJson['task_selected_docs'] #id
    task_title = requestJson['task_title']
    #task_dataset = requestJson['task_dataset'] # id   
    task_description = requestJson['task_description']    
        
    # adjust host setting, depending on whether HIT is live (production) or in testing mode (sandbox)
    mode = "sandbox"
    # mode ="production"

    if mode=="production":
        HOST='mechanicalturk.amazonaws.com'
    else:
        HOST='mechanicalturk.sandbox.amazonaws.com'

    mtc = MTurkConnection(aws_access_key_id= user_aws_access_key_id,
                      aws_secret_access_key= user_aws_secret_key,
                      host=HOST)
                      
    overview = Overview()
    overview.append_field('Title', task_title)
    overview.append(FormattedContent('<p>' + task_description + '</p>'))

    overview.append(FormattedContent('<table>'))
    for docID in task_selected_docs:
        docText = Doc.objects.get(pk = docID)
        overview.append(FormattedContent('<tr><td>' + docText.text + '</td></tr>')) 
    overview.append(FormattedContent('</table>'))    
    
    
    return HttpResponse(json.dumps({'data' : mtc.get_account_balance():}), content_type = "application/json")

	# return TemplateResponse(request, 'myturk/createhit.html', context)



