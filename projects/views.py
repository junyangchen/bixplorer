from django.shortcuts import render
from django.template.response import TemplateResponse
from django.conf import settings
from projects.models import Project, Comment
from itertools import chain
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse

def index(request):
    context = { 'active_tag': 'home', 'BASE_URL':settings.BASE_URL}
    return TemplateResponse(request, 'projects/index.html', context)

@csrf_protect   
def add(request):
    if request.method == 'GET':
        context = { 'active_tag': 'home', 'BASE_URL':settings.BASE_URL}
        return TemplateResponse(request, 'projects/add.html', context)  
    elif request.method == 'POST':
        print 'Raw Data: "%s"' % request.body   
        return HttpResponse(request.body.project_name)
      
    
def detail(request, project_id):
    theproject = Project.objects.get(id = project_id)
    allComments =    Comment.objects.all();
    selectedComments = allComments.filter(user = request.user)
    # if theproject.is_creator(request.user):
        #List all comments of this project that are not deleted
        # comments = Comment.objects.filter( project = theproject)
        #comments = Comment.objects.filter( project = theproject).filter( is_deleted = '0' )
        # iscreate = True
    # else:
        #List comments created by a user that are not deleted
        # comments = Comment.objects.filter( user = request.user).filter(project = theproject)
        #comments = Comment.objects.filter( user = request.user).filter( is_deleted = '0' )
        # iscreate = False
        
    
    # known_ids = set()
    # comments = []
    # for element in comments1:
        # if element.id not in known_ids:
                # known_ids.add(element.id)
                # comments.append(element)
               
    context = { 'user' : request.user, 'BASE_URL':settings.BASE_URL, 'project' : theproject, 'comments': selectedComments}
    return TemplateResponse(request, 'projects/detail.html', context)