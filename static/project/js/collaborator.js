
// remove a collaborator
$('.remove_collaborators').click(function() {
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
});


$('#btn_collaborator_add').click(function(){
	var csrftoken = $('#csrf_token').val();
	var collaborator_name = $('#collaborator_name').val(),
		projectID = $('#projectID_token').val();

    var requestJSON = {
		"project_id": projectID,
    	"collaborator_name": collaborator_name,
    }

    $.ajax({
        url: window.SERVER_PATH + "projects/collaborator/add/",
        type: "POST",
        data: JSON.stringify(requestJSON),
        contentType: "application/json",
        success: function(data){
            var resData = eval(data);
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


// these HTTP methods do not require CSRF protection
function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}


function refreshColList(colListID, collaborators) {
    // remove previous element
    $(colListID).empty();
    console.log(collaborators);
    // refresh the elements
    for (var i = 0; i < collaborators.length; i++)
        $(colListID).prepend('<li class="list-group-item" id="col_list_id">'+
            '<div class="row">'+
                '<div class="col-xs-3 col-md-2 left_15_gap">'+
                    '<img src="' + window.PUBLIC_PATH + 'common/imgs/default.jpg" class="img-circle img-responsive" alt="" />'+
                '</div>'+
                '<div class="col-xs-6 col-md-8">'+
                    '<p>' + collaborators[i][0]['collaborator'] + '</p>'+
                    '<div class="mic-info">' + collaborators[i][1]['email'] + '</div>'+
                '</div>'+
                '<div class="col-xs-2 col-md-1">'+
                    '<span class="glyphicon glyphicon-remove remove_collaborators" title="{{ collaborator.username }}"></span>'+
                '</div>'+
            '</div>'+
        '</li>');
}


/*
* Click event for add and remove button
* @param btn, the function of the button
*/
function clickEvent(btn) {
    
}