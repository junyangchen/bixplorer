from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpResponseNotAllowed
from django.conf import settings
from projects.models import Project, Comment, DataSet
from itertools import chain
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.utils import timezone
import json

def index(request):
    context = { 'active_tag': 'home', 'BASE_URL':settings.BASE_URL}
    return TemplateResponse(request, 'projects/index.html', context)

@csrf_protect   
def add(request):
    if request.method == 'GET':
        dataset = DataSet.objects.all()
        context = { 'active_tag': 'home', 'BASE_URL':settings.BASE_URL, 'dataset': dataset}
        return TemplateResponse(request, 'projects/add.html', context)  
    elif request.method == 'POST':
        print 'Raw Data: "%s"' % request.body
        # parse from front end
        projectRaw = json.loads(request.body)
        
        
        try:
            newProject = Project(user = request.user, dataset = DataSet.objects.get(id = projectRaw['dataset_id']), 
                name = projectRaw['project_name'], description = projectRaw['project_description'], 
                create_time = timezone.now(), is_private = projectRaw['project_privacy'], 
                is_deleted = 0)
            
            newProject.save()
            
            responseData = {'status':'success'}
        except:
            responseData = {'status':'failed'}
        
        # serialize for front end
        newData = json.dumps(projectRaw)
        return HttpResponse(json.dumps(responseData), content_type = "application/json")
        #return HttpResponse(json.dumps(responseData))
        
@csrf_protect
def edit(request, project_id):
    if request.method != 'GET':
        return HttpResponseNotAllowed('Only GET here')
    
    theUser = request.user
        
    # Load project data from the database
    project = Project.objects.get(id = project_id)
    
    # check user permission
    # Only the project creator, super user and moderator can edit the project
    
    
    
    # Load data set list from the database
    
    
    return HttpResponse(project_id)
        
def plist(request):
    if request.method == 'GET':
        # Retrieve projects list from database
        projectList = Project.objects.filter(user = request.user)
        context = { 'user' : request.user, 'BASE_URL':settings.BASE_URL, 'projects' : projectList}
    return TemplateResponse(request, 'projects/plist.html', context)

    
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
               
    context = { 'user' : request.user, 'BASE_URL':settings.BASE_URL, 'project' : theproject, 'comments': allComments}
    return TemplateResponse(request, 'projects/detail.html', context)