
// remove a collaborator
$('.remove_collaborators').click(function() {
    var csrftoken = $('#csrf_token').val();
    var projectID = $('#projectID_token').val();
    var selectedColUser = $(this).prop('title');
    var selectedColID = $(this)

    var requestJSON = {
        "project_id": projectID,
        "collaborator_name": selectedColUser
    }

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajax({
        url: window.SERVER_PATH + "projects/collaborator/delete/",
        type: "POST",
        data: JSON.stringify(requestJSON),
        contentType: "application/json",
        success: function(data){
            console.log(data);
            // if(data['status'] == 'success') {
            //     window.location = window.SERVER_PATH + "projects/plist/";
            // }

            // hide the popup
            $(selectedColID).remove();
        },
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });  
})


$('#btn_collaborator_add').click(function(){
	var csrftoken = $('#csrf_token').val();
	var collaborator_name = $('#collaborator_name').val(),
		projectID = $('#projectID_token').val();

    var requestJSON = {
		"project_id": projectID,
    	"collaborator_name": collaborator_name,
    }

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajax({
        url: window.SERVER_PATH + "projects/collaborator/add/",
        type: "POST",
        data: JSON.stringify(requestJSON),
        contentType: "application/json",
        success: function(data){
            console.log(data);
            // if(data['status'] == 'success') {
            //     window.location = window.SERVER_PATH + "projects/plist/";
            // }
            //$('#list_collaborator').prepend('<li class="list-group-item" id="col_list_id"><div class="row"><div class="col-xs-3 col-md-2 left_15_gap"><img src="' + window.PUBLIC_PATH + 'common/imgs/default.jpg" class="img-circle img-responsive" alt="" /></div></div></li>');
        },
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });	
})