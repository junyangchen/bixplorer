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

    # overview.append(FormattedContent('<table><tr><td>test</td><td>try</td></tr><tr><td>5</td><td>7</td></tr></table>'))

    tableStr = '<table>'
    for docID in task_selected_docs:
        docText = Doc.objects.get(pk = docID)
        tableStr += '<tr><td>' + docText.text + '</td></tr>'
    tableStr += '</table>' 

    overview.append(FormattedContent(tableStr))

    # overview.append(FormattedContent('<table>'))
    # # # for docID in task_selected_docs:
    # # #     docText = Doc.objects.get(pk = docID)
    # # #     overview.append(FormattedContent('<tr><td>' + docText.text + '</td></tr>')) 
    # overview.append(FormattedContent('</table>'))    

    qc2 = QuestionContent()
    qc2.append_field('Title','What is the plan?')
     
    fta2 = FreeTextAnswer()
     
    q2 = Question(identifier="comments",
                  content=qc2,
                  answer_spec=AnswerSpecification(fta2))
     
    #--------------- BUILD THE QUESTION FORM -------------------
     
    question_form = QuestionForm()
    question_form.append(overview)
    question_form.append(q2)
     
    #--------------- CREATE THE HIT -------------------
     
    creathitReturnValue = mtc.create_hit(questions=question_form,
                                                       max_assignments=10,
                                                       title=task_title,
                                                       description=task_description,
                                                       keywords='SomeKeywords',
                                                       duration = 60*5,
                                                       reward=0.05)

    
    
    return HttpResponse(json.dumps({'data' : mtc.get_account_balance()}), content_type = "application/json")

    # return TemplateResponse(request, 'myturk/createhit.html', context)


def hitresult(request):
 
    context = { 'active_tag': 'myturk', 'BASE_URL':settings.BASE_URL}  
    return TemplateResponse(request, 'myturk/hitResult.html', context)


def hitresultfetch(request):
    from boto.mturk.question import QuestionContent,Question,QuestionForm,Overview,AnswerSpecification,SelectionAnswer,FormattedContent,FreeTextAnswer

    import mturk_getallreviewablehits as getAllHits

    requestJson = json.loads(request.body)    
    
    user_aws_secret_key = requestJson['aws_secret_key']    
    user_aws_access_key_id = requestJson['aws_access_key_id']

    # return TemplateResponse(request, 'myturk/hitResult.html', context)

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





    allHits = getAllHits.get_all_reviewable_hits(mtc)

    print('how many hits in allHits')
    print(len(allHits))

    ## todo get hit content
    print('------before looping through allHits')
    for hit in allHits:
        assignments=mtc.get_assignments(hit.HITId)
        print(hit)
        print(hit.HITId)

        print('assignments in a hit:')
        print(assignments)

        dir(assignments)

        # print(assignments.Request)
        # print(assignments.Assignment)
        # print(assignments.HIT)

        for assignment in assignments:
            print("Answers of the worker %s" % assignment.WorkerId)
            for question_form_answer in assignment.answers[0]:
                # for key, value in question_form_answer.fields:
                #     print "%s: %s" % (key,value)
                #     print(value)
                for value in question_form_answer.fields:
                    print(value)


            print ("--------------------")
            
    print('------after looping through allHits')


    return HttpResponse({'hitresult key':'thevaluefromhitresult'}, content_type = "application/json")


