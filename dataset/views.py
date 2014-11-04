from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from dataset.models import DataSet, Doc
import json

# Create your views here.
def index():
    return HttpResponse("Under construction!")

def load_datasets_json(request):
    ''' Helper function for loading all datasets
        from the database
    '''
    # if not request.method == 'POST':
        # raise Http404
    
    try:
        datasets = get_list_or_404(DataSet)
        for item in datasets:
            print item
        # Check permission
        # theUser = request.user
        # if not (theproject.is_creator(theUser) or theUser.isupper or 
            # theproject.is_collaborator(theUser)):
            # raise Http404
        datasets_list = [] 
        for dataset in datasets:
            tmp = []        
            tmp.append({'name': dataset.name})
            tmp.append({'dataset_id': dataset.id})
            tmp.append({'create_time': str(dataset.create_time)})
            datasets_list.append(tmp)        
    except Exception as e:
        print e
        
    responseData = {'status':'success', 'datasets': datasets_list}
    return HttpResponse(json.dumps(responseData), content_type = "application/json")  
    
def load_docs_by_datasetId(request):
    ''' Helper function for loading all datasets
        from the database
    '''
    # if not request.method == 'POST':
        # raise Http404
        
    try:
        datasetID = 2 #request['dataset_id']
        docs = get_list_or_404(Doc, dataset_id = datasetID)
        # Check permission
        # theUser = request.user
        # if not (theproject.is_creator(theUser) or theUser.isupper or 
            # theproject.is_collaborator(theUser)):
            # raise Http404
        docs_list = [] 
        for doc in docs:
            tmp = []        
            tmp.append({'name': doc.people})
            tmp.append({'dataset_id': doc.location})
            tmp.append({'create_time': doc.organization})
            docs_list.append(tmp)     
        responseData = {'status':'success', 'docs': docs_list}            
    except Exception as e:
        print e
    
    
    return HttpResponse(json.dumps(responseData), content_type = "application/json")  
    