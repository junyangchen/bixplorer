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
import json
from home.utils import * 

from boto.mturk.connection import MTurkConnection

import connectMturk as mtconnection
from boto.mturk.question import QuestionContent,Question,QuestionForm,Overview,AnswerSpecification,SelectionAnswer,FormattedContent,FreeTextAnswer
from dataset.models import Doc

def index(request):
	context = 'Test the response to index page'
	return TemplateResponse(request, 'myturk/index.html', context)

def createhit(request):

	# adjust host setting, depending on whether HIT is live (production) or in testing mode (sandbox)
	mode = "sandbox"
	# mode ="production"
	if mode=="production":
	    HOST='mechanicalturk.amazonaws.com'
	else:
	    HOST='mechanicalturk.sandbox.amazonaws.com'

	HOST = 'mechanicalturk.sandbox.amazonaws.com'

	mtc = MTurkConnection(aws_access_key_id=ACCESS_ID,
	                      aws_secret_access_key=SECRET_KEY,
	                      host=HOST)

	print mtc.get_account_balance()

	requestJson = json.loads(request.body)


	title = requestJson['title']
	description = requestJson['description']
	docIds = requestJson['docIds']
	AWSAccessKeyId = requestJson['AWSAccessKeyId']
	AWSSecretKey = requestJson['AWSSecretKey']

	 
	overview = Overview()
	overview.append_field('Title', 'Give your adfadfadfadfafafafadsf')

	overview.append(FormattedContent('<link href="https://s3.amazonaws.com/mturk-public/bs30/css/bootstrap.min.css" rel="stylesheet" />'

									'</section>'))
	




	 
	qc2 = QuestionContent()
	qc2.append_field('Title','What is the plan?')
	 
	fta2 = FreeTextAnswer()
	 
	q2 = Question(identifier="comments",
	              content=qc2,
	              answer_spec=AnswerSpecification(fta2))
	 
	#--------------- BUILD THE QUESTION FORM -------------------
	 
	question_form = QuestionForm()
	question_form.append(overview)
	question_form.append(q1)
	question_form.append(q2)
	 
	#--------------- CREATE THE HIT -------------------
	 
	creathitReturnValue = mtconnection.mtc.create_hit(questions=question_form,
										               max_assignments=10,
										               title=title,
										               description=description,
										               # keywords=keywords,
										               duration = 60*5,
										               reward=0.05)

	print(creathitReturnValue)








    # Load dataset from database
    datasets = DataSet.objects.all()    
    context = { 'active_tag': 'myturk', 'BASE_URL':settings.BASE_URL, 'datasets':datasets}
    return TemplateResponse(request, 'myturk/createhit.html', context)

def testcreatehit(request):
	context = 'Test the response to createhit page'
	return TemplateResponse(request, 'myturk/createhit.html', context)


