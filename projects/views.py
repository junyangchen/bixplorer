from django.shortcuts import render, get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.http import HttpResponseNotAllowed, HttpResponseForbidden
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
        # parse from front end
        projectRaw = json.loads(request.body)
        
        # Handle the request from edit view
        if projectRaw.has_key('project_id') and projectRaw['project_id'].isdigit():
            # TO-DO validate the data
            try:
                theUser = request.user
                # Load project data from the database                
                toUpdate = Project.objects.get(pk = projectRaw['project_id'])
                
                # TO-DO check if the project is delted
                
                # Only the project creator, super user and collaborators can edit the project
                has_permission = toUpdate.is_creator(theUser) or toUpdate.is_collaborator(theUser) or theUser.is_superuser
    
                if not has_permission:
                    return HttpResponseForbidden("You dont' have the permission to edit this project!")    
                
                toUpdate = Project.objects.get(pk = projectRaw['project_id'])
                toUpdate.dataset = DataSet.objects.get(id = projectRaw['dataset_id'])
                toUpdate.name = projectRaw['project_name']
                toUpdate.description = projectRaw['project_description']
                toUpdate.is_private = projectRaw['project_privacy']
                toUpdate.save()
                responseData = {'status':'success'}
            except:
                responseData = {'status':'fail'}
        # Handle request from the add view    
        else:     
            try:
                newProject = Project(user = request.user, dataset = DataSet.objects.get(id = projectRaw['dataset_id']), 
                    name = projectRaw['project_name'], description = projectRaw['project_description'], 
                    create_time = timezone.now(), is_private = projectRaw['project_privacy'], 
                    is_deleted = 0)
            
                newProject.save()
            
                responseData = {'status':'success'}
            except:
                responseData = {'status':'fail'}
        
        # return status back to front end
        return HttpResponse(json.dumps(responseData), content_type = "application/json")
        #return HttpResponse(json.dumps(responseData))
        
@csrf_protect
def edit(request, project_id):
    if request.method == 'GET':
        datasets = DataSet.objects.all()
        project = Project.objects.get(id = project_id)
        context = { 'active_tag': 'home', 'BASE_URL':settings.BASE_URL, 'datasets': datasets, 'selectedDatasetID':project.dataset.id, 'project': project}
        return TemplateResponse(request, 'projects/edit.html', context)
        
    # TO-DO    
    elif request.method == 'POST':    
        theUser = request.user
        
        # Load project data from the database
        project = Project.objects.get(id = project_id)
    
        # check user permission
        # Only the project creator, super user and collaborators can edit the project
        has_permission = project.is_creator(theUser) or project.is_collaborator(theUser) or theUser.is_superuser
    
        if not has_permission:
            return HttpResponseForbidden("You dont' have the permission to edit this project!")
            
        # Load data set list from the database    
        return HttpResponse(has_permission)
    
    else:
        return HttpResponseForbidden("Error 405. Only GET and POST allowed for this view.")

def delete(request, project_id):
    theUser = request.user
    # Load project data from the database                
    toDelete = Project.objects.get(pk = project_id)
    
    # Only the project creator, super user can delete the project
    has_permission = toDelete.is_creator(theUser) or toDelete.is_collaborator(theUser) or theUser.is_superuser
    
    if not has_permission:
        return HttpResponseForbidden("You dont' have the permission to delete this project!")
    
    try:
        toDelete.is_deleted = 1
        toDelete.save()
        return redirect('/projects/plist/')
    except:
        # TO-DO show error message
        responseData = {'status':'fail'}    
    
    
        
def plist(request):
    if request.method == 'GET':
        # Retrieve projects list from database
        projectList = Project.objects.filter(user = request.user).filter(is_deleted = '0')
        context = { 'user' : request.user, 'BASE_URL':settings.BASE_URL, 'projects' : projectList}
    return TemplateResponse(request, 'projects/plist.html', context)

    
def detail(request, project_id):
    theproject = Project.objects.get(id = project_id)
    allComments =    theproject.comment.all();
    for comment in allComments:
        if comment.user == request.user:
            comment.edit_enable = True
        else:
            comment.edit_enable = False
    
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
    
def addCollaborator(request, project_id):
    theproject = Project.objects.get(id = project_id)

     