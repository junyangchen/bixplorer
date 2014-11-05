from django.shortcuts import render, get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.http import HttpResponseNotAllowed, HttpResponseForbidden, Http404
from django.conf import settings
from projects.models import Project, Comment, DataSet, Collaborationship
from itertools import chain
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.models import User
import json
from home.utils import * 
    
from django.contrib.auth.decorators import login_required 

@login_required   
def index(request):
    theUser = request.user
    # Load the total number of projects for the user
    collaborationShip = Collaborationship.objects.filter(user = theUser)
    private_projects = Project.objects.filter(user = theUser, is_private = 1)
    public_projects = Project.objects.filter(is_private = 0)
    
    # Calculate the number of projects for the user
    project_set = set()
    count = 0 
    
    try:
        for item in collaborationShip:
            if str(item.project.id) not in project_set:
                project_set.add(str(item.project.id))
                count += 1
        for item in private_projects:
            print item.name
            if not item.name in project_set:
                project_set.add(item.name)
                count += 1
        for item in public_projects:
            if item.id not in project_set:
                project_set.add(str(item.id))
                count += 1
                
    except Exception as e:
        return HttpResponse(e)
        print e
        
    context = { 'active_tag': 'home', 'BASE_URL':settings.BASE_URL, 'count': count}
    return TemplateResponse(request, 'projects/index.html', context)

@csrf_protect   
def add(request):
    if request.method == 'GET':
        dataset = DataSet.objects.all()
        context = { 'active_tag': 'projects', 'BASE_URL':settings.BASE_URL, 'dataset': dataset}
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
                
                if is_private_front_end == '1':
                    print is_private_front_end                    
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
        theUser = request.user
        
        # Load the total number of projects for the user
        collaborationShip = Collaborationship.objects.filter(user = theUser).filter(is_deleted = '0')
        my_projects_queryset = Project.objects.filter(user = theUser)
        public_projects_queryset = Project.objects.filter(is_private = 0)
        
        # Calculate the number of projects for the user
        project_set = set()
        shared_projects = []
        public_projects = []
        count = 0 
        
        try:
            for item in my_projects_queryset:
                if not item.id in project_set:
                    project_set.add(item.id)
                    count += 1
            
            for item in collaborationShip:
                if not item.project.id  in project_set:
                    project_set.add(str(item.project.id))
                    shared_projects.append(item.project)
                    count += 1
                    
            for item in public_projects_queryset:
                if not item.id in project_set:
                    project_set.add(str(item.id))
                    public_projects.append(item)
                    count += 1
                    
        except Exception as e:
            return HttpResponse(e)
            print e
        
        
    context = { 'active_tag': 'projects', 'user' : request.user, 'BASE_URL':settings.BASE_URL, 
        'my_projects' : my_projects_queryset, 'shared_projects' : shared_projects, 'public_projects': public_projects}
    return TemplateResponse(request, 'projects/plist.html', context)

@login_required    
def detail(request, project_id):
    theproject = Project.objects.get(id = project_id)
    allComments =    theproject.comment_set.all();
    allComments = allComments.filter(is_deleted = False)  
    for comment in allComments:
        # TO-DO
        if comment.user == request.user:
            comment.edit_enable = True
        else:
            comment.edit_enable = False
    
    collaborators = []
    # Only project creator, collaborator and super user can
    # have access to the collaborators
    # perm = 0, user will not see the collaborator view
    # perm = 1, a user will see the collaborator view, but can not edit or add
    # perm = 2, a user will be able to edit or add collaborators
    perm = 0
    theUser = request.user
    if theproject.is_creator(theUser) or theUser.is_superuser:
        perm = 2
    elif theproject.is_collaborator(theUser):
        perm = 1
    else:
        perm = 0
    
    # Load collaborators
    if not perm == 0:
        collaboratorShip = Collaborationship.objects.filter(is_deleted = 0, project = theproject).exclude(user = theUser)    
        for collaborator in collaboratorShip:
            collaborators.append(collaborator.user)
            
    context = { 'user' : request.user, 'BASE_URL':settings.BASE_URL, 
        'project' : theproject, 'comments': allComments, 
        'collaborators':collaborators, 'permisson' : perm}
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
        tmp = {}
        tmp = {'user':request.user.username,'content':comment.content,
                'comment_id':comment.id, 'project_id':project_id, 'pub_date': str(comment.create_time)}
        # check edit or delete permissions
        if comment.user == request.user:            
            tmp['edit_enable'] = True
        else:
            tmp['edit_enable'] = False
        comments_list.append(tmp)    
    return comments_list  

def load_project_collaborators_json(request, project_id):
    ''' Helper function for loading collaborators
        Only the project owner, collaborators and
        super user can request the collaborators
    '''
    try:
        theproject = get_object_or_404(Project, pk = project_id)

        # Check permission
        theUser = request.user
        if not (theproject.is_creator(theUser) or theUser.isupper or 
            theproject.is_collaborator(theUser)):
            raise Http404

            
        collaboratorShip = Collaborationship.objects.filter(is_deleted = 0, project = theproject).exclude(user = theUser)
        collaborators = []
        for collaborator in collaboratorShip:
            if collaborator.user.is_active:
                collaborators.append(collaborator.user)
                
        collaborators_list = [] 
        for collaborator in collaborators:
            collaborators_list.append({'collaborator': collaborator.username, 'email': collaborator.email
                ,'collaborator_id': collaborator.id, 'project_id':project_id})
    except Exception as e:
        print e       
        
    return collaborators_list      
    
def add_comment(request):
    if request.method == 'POST':
        # parse from front end
        projectRaw = json.loads(request.body)
        try:
            theUser = request.user
            project_id = projectRaw['project_id']      
            # Load project data from the database                
            toUpdate = Project.objects.get(pk = projectRaw['project_id'])
            
            # check if the project is delted
            if toUpdate.is_deleted:
                raise Http404
            
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
            comments_json = load_project_comment_json(request, project_id)
            responseData = {'status':'success', 'comments': comments_json}
            return HttpResponse(json.dumps(responseData), content_type = "application/json")
        except Exception as e:
            print e
            raise Http404
                
    
    
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
    '''
    Handles request for adding a collaborator to a project.
    Request data is sent by POST.
    '''
    if request.method == 'POST':
        # request json data
        projectRaw = json.loads(request.body)
        try:
            project_id = projectRaw['project_id']
            collaborator_name = projectRaw['collaborator_name']
            theUser = request.user
            
            # TO-DO handle situations when collaborator_name does not exist
            collaborator = get_object_or_404(User, username = collaborator_name)
            
            if collaborator == theUser:
                raise Http404
            
            theProject = get_object_or_404(Project, pk = project_id)
            # check if the project is delted
            if theProject.is_deleted:
                raise Http404
            
            # Only the project creator and supper user can add collaborators of the project
            has_permission = theProject.is_creator(theUser) or theUser.is_superuser

            if not has_permission:
                raise Http404
            # Add the collaborator to the project
            sc = None
            try:
                sc = Collaborationship.objects.get(project = theProject, user = collaborator, is_deleted = True)
            except:
                pass
            if not sc == None:                
                newCollaborationship = sc
                newCollaborationship.is_deleted = False
            else:    
                newCollaborationship = Collaborationship(project = theProject, user = collaborator)
            newCollaborationship.save()
                
            # Log project change actions
            # log_addition(request, collaborator)              
            
            # Reload the collaborators from the database
            collaborators_list = load_project_collaborators_json(request, project_id)
            responseData = {'status':'success', 'collaborators': collaborators_list}
            return HttpResponse(json.dumps(responseData), content_type = "application/json")
        except Exception as e:      
            print e
            raise Http404
    else:
        raise Http404
        
def delete_collaborator(request):    
    if request.method == 'POST':
        collaboratorRaw = json.loads(request.body)
        try:            
            project_id = collaboratorRaw['project_id']
            collaborator_name = collaboratorRaw['collaborator_name']
            theUser = request.user
            # TO-DO handle situations when collaborator_name does not exist
            collaborator = get_object_or_404(User, username = collaborator_name)
            
            # TO-DO send feedback
            if theUser == collaborator:
                raise Http404
            
            theProject = get_object_or_404(Project, pk = project_id) 
            
            # check if the project is delted or if the collaborator bellongs to the project
            if theProject.is_deleted or (not theProject.is_collaborator(collaborator)):
                raise Http404    
                
            # Only the project creator, super user can delete collaborator of the project
            has_permission = theProject.is_creator(theUser) or theUser.is_superuser
            
            if not has_permission:
                raise Http404
            
            collaborationship = Collaborationship.objects.get(project = theProject, user = collaborator)
            collaborationship.is_deleted = True
            collaborationship.save()  
            obj_display = force_text(collaborationship)
            log_deletion(request, collaborationship, obj_display)
            
            '''
            theComment.is_deleted = True
            theComment.save()    
            obj_display = force_text(theComment)
            log_deletion(request, theComment, obj_display)'''           
            
            
            # Reload the collaborators from the database
            collaborators_list = load_project_collaborators_json(request, project_id)
            responseData = {'status':'success', 'collaborators': collaborators_list}
            return HttpResponse(json.dumps(responseData), content_type = "application/json")
        except Exception as e:
            print e
            raise Http404
    else:
        raise Http404