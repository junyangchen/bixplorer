from django.shortcuts import render, get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.http import HttpResponseNotAllowed, HttpResponseForbidden
from django.conf import settings
from projects.models import Project, Comment, DataSet
from itertools import chain
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.models import User
import json
from home.utils import * 
    
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
                is_private_front_end = projectRaw['project_privacy']
                if is_private_front_end == 'True':
                    toUpdate.is_private = True
                else:
                    toUpdate.is_private = False
                    
                toUpdate.save()
                # Log the change
                change_msg = toUpdate.construct_change_message()
                log_change(request, toUpdate, change_msg)
                # return HttpResponse(str(change_msg))
                responseData = {'status':'success'}
            except Exception as e:
                return HttpResponse(e)
                responseData = {'status':'fail'}
        # Handle request from the add view    
        else:     
            try:
                newProject = Project(user = request.user, dataset = DataSet.objects.get(id = projectRaw['dataset_id']), 
                    name = projectRaw['project_name'], description = projectRaw['project_description'], 
                    create_time = timezone.now(), is_private = projectRaw['project_privacy'], 
                    is_deleted = 0)
            
                newProject.save()
                
                # Log project change actions
                log_addition(request, newProject)              
            
                responseData = {'status':'success'}
            except Exception as e:
                return HttpResponse(e)
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
        toDelete.is_deleted = True
        toDelete.save()
        obj_display = force_text(toDelete)
        log_deletion(request, toDelete, obj_display)
        return redirect('/projects/plist/')
    except Exception as e:
        return HttpResponse(e) 
    
    
        
def plist(request):
    if request.method == 'GET':
        # Retrieve projects list from database
        # Should use request.user.id to fix simpleLazyObject error
        projectList = Project.objects.filter(user = request.user.id).filter(is_deleted = '0')
        
        # TO-DO define three class of projects
        
        context = { 'user' : request.user, 'BASE_URL':settings.BASE_URL, 'projects' : projectList}
    return TemplateResponse(request, 'projects/plist.html', context)

    
def detail(request, project_id):
    theproject = Project.objects.get(id = project_id)
    allComments =    theproject.comment_set.all();
    allComments = allComments.filter(is_deleted = False)  
    for comment in allComments:
        if comment.user == request.user:
            comment.edit_enable = True
        else:
            comment.edit_enable = False
            
    context = { 'user' : request.user, 'BASE_URL':settings.BASE_URL, 'project' : theproject, 'comments': allComments}
    return TemplateResponse(request, 'projects/detail.html', context)
    
def addCollaborator(request, project_id):
    theproject = Project.objects.get(id = project_id)

def load_project_comment_json(request, project_id):
    ''' Helper function for loading comments'''
    theproject = get_object_or_404(Project, pk = project_id)
    allComments =    theproject.comment_set.all();
    allComments = allComments.filter(is_deleted = False)
    
    comments_list = [] 
    for comment in allComments:
        comments_list.append({'user':request.user.username})
        comments_list.append({'content':comment.content})
        comments_list.append({'comment_id':comment.id})
        comments_list.append({'project_id':project_id})
        comments_list.append({'pub_date': str(comment.create_time)})
        # check edit or delete permissions
        if comment.user == request.user:            
            comments_list.append({'edit_enable': True})
        else:
            comments_list.append({'edit_enable': False})
    return comments_list  
    
    
def add_comment(request, project_id):
    if request.method == 'POST':
        # parse from front end
        projectRaw = json.loads(request.body)
        try:
            theUser = request.user
            # Load project data from the database                
            toUpdate = Project.objects.get(pk = projectRaw['project_id'])
            
            # check if the project is delted
            if toUpdate.is_deleted:
                responseData = {'status':'fail'}
                return HttpResponse(json.dumps(responseData), content_type = "application/json")
            
            # Check user permission for adding a comment
            if not toUpdate.is_private:
                has_permission = True            
            else:
                # Only the project creator, super user and collaborators can add comment to the project
                has_permission = toUpdate.is_creator(theUser) or toUpdate.is_collaborator(theUser) or theUser.is_superuser

            if not has_permission:
                responseData = {'status':'fail'}
                return HttpResponse(json.dumps(responseData), content_type = "application/json")
                #return HttpResponseForbidden("You dont' have the permission to edit this project!")  
            
            newComment = Comment(project = toUpdate, user = request.user, 
                    content = projectRaw['content'],
                    create_time = timezone.now(),
                    is_deleted = 0)
            
            newComment.save()
                
            # Log project change actions
            log_addition(request, newComment)              
            
            # Prepare the return json data
            
            
            responseData = {'status':'success'}
        except Exception as e:
            raise Http404
                
    return HttpResponse(json.dumps(responseData), content_type = "application/json")
    
def delete_comment(request):
    if request.method == 'POST':
        projectRaw = json.loads(request.body)
        try:
            project_id = projectRaw['project_id']
            comment_id = projectRaw['comment_id']
            theUser = request.user
            # Load project data from the database                
            theProject = get_object_or_404(Project, pk = project_id)
            theComment = get_object_or_404(Comment, pk = comment_id)
            
            # check if the project is delted
            if theProject.is_deleted or theComment.is_deleted:
                raise Http404
            # Only the project creator, super user and collaborators can delete comment of the project
            has_permission = theProject.is_creator(theUser) # or theProject.is_collaborator(theUser) or theUser.is_superuser or theComment.is_creator(theUser)

            if not has_permission:
                raise Http404
            theComment.is_deleted = True
            theComment.save()    
            obj_display = force_text(theComment)
            log_deletion(request, theComment, obj_display)
            
            
            # Reload the comments from the database
            comments_json = load_project_comment_json(request, project_id)
            responseData = {'status':'success', 'comments': comments_json}
            return HttpResponse(json.dumps(responseData), content_type = "application/json")
        except Exception as e:        
            raise Http404
    else:
        raise Http404

        
        
def add_collaborator(request):
    if request.method == 'POST':
        projectRaw = json.loads(request.body)
        try:
            project_id = projectRaw['project_id']
            collaborator_name = projectRaw['collaborator_name']
            theUser = request.user
            collaborator = get_object_or_404(User, username = collaborator_name)
            theProject = get_object_or_404(Project, pk = project_id)
            # check if the project is delted
            if theProject.is_deleted:
                raise Http404
    
            # Only the project creator and supper user can add collaborators of the project
            has_permission = theProject.is_creator(theUser) or theUser.is_superuser

            if not has_permission:
                raise Http404
            # Add the collaborator to the project
            theProject.collaborators.add(collaborator)
            theProject.save()
                
            # Log project change actions
            # log_addition(request, collaborator)              
            
            responseData = {'status':'success'}
            return HttpResponse(json.dumps(responseData), content_type = "application/json")
        except Exception as e:        
            raise Http404
    else:
        raise Http404