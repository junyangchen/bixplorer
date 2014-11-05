
// remove a collaborator
$('.remove_collaborators').click(function() {
    // btnClickEvent('delete');
    
    var csrftoken = $('#csrf_token').val();
    var projectID = $('#projectID_token').val();
    var selectedColUser = $(this).prop('title');

    var requestJSON = {
        "project_id": projectID,
        "collaborator_name": selectedColUser
    }

    $.ajax({
        url: window.SERVER_PATH + "projects/collaborator/delete/",
        type: "POST",
        data: JSON.stringify(requestJSON),
        contentType: "application/json",
        success: function(data){
            if(data['status'] == 'success') {
                refreshColList('#list_collaborator', data['collaborators']);
            }
        },
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });  
});

$('#btn_collaborator_add').click(function(){
    btnClickEvent('add');
    // empty the input
    $('#collaborator_name').val('');	
});


// these HTTP methods do not require CSRF protection
function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}


/*
* Refresh the collaborator list
* @param colListID, ID of the collaborator list
* @param collaborators, the array of collaborators
*/
function refreshColList(colListID, collaborators) {
    // cancel ajax
    $.ajaxSetup({async:false});

    // remove previous element
    $(colListID).empty();

    // refresh the elements
    for (var i = 0; i < collaborators.length; i++) {
        var del = '<span class="glyphicon glyphicon-remove remove_collaborators" title="' + collaborators[i]['collaborator'] + '"></span>';
        $(colListID).prepend('<li class="list-group-item" id="col_list_id">'+
            '<div class="row">'+
                '<div class="col-xs-3 col-md-2 left_15_gap">'+
                    '<img src="' + window.PUBLIC_PATH + 'common/imgs/default.jpg" class="img-circle img-responsive" alt="" />'+
                '</div>'+
                '<div class="col-xs-6 col-md-8">'+
                    '<p>' + collaborators[i]['collaborator'] + '</p>'+
                    '<div class="mic-info">' + collaborators[i]['email'] + '</div>'+
                '</div>'+
                '<div class="col-xs-2 col-md-1">'+
                    del + 
                '</div>'+
            '</div>'+
        '</li>');    
    }

    // update the number of collaborators
    $('#col_num').html(collaborators.length);

    // rebinde the click event for those new appended elements
    $('.remove_collaborators').click(function(){
        var csrftoken = $('#csrf_token').val();
        var projectID = $('#projectID_token').val();
        var selectedColUser = $(this).prop('title');

        var requestJSON = {
            "project_id": projectID,
            "collaborator_name": selectedColUser
        }

        $.ajax({
            url: window.SERVER_PATH + "projects/collaborator/delete/",
            type: "POST",
            data: JSON.stringify(requestJSON),
            contentType: "application/json",
            success: function(data){
                console.log(data);
                if(data['status'] == 'success') {
                    refreshColList('#list_collaborator', data['collaborators']);
                }
            },
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        }); 
    })
}


/*
* Click event for add and remove button
* @param btn, the function of the button
*/
function btnClickEvent(btn) {
    var csrftoken = $('#csrf_token').val();
    var projectID = $('#projectID_token').val(),
        collaboratorName = '';

    if (btn == 'add')
        collaboratorName = $('#collaborator_name').val();
    // else if (btn == 'delete') {
    //     console.log('here');
    //     collaboratorName = $(this).prop('title');
    // }

    var requestJSON = {
        "project_id": projectID,
        "collaborator_name": collaboratorName
    }    

    $.ajax({
        url: window.SERVER_PATH + 'projects/collaborator/' + btn + '/',
        type: "POST",
        data: JSON.stringify(requestJSON),
        contentType: "application/json",
        success: function(data){
            if(data['status'] == 'success') {
                refreshColList('#list_collaborator', data['collaborators']);
            }
        },
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });    
}