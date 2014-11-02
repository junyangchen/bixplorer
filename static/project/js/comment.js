
// show popup for confirming deletion
$('.btn_comment_delete').click(function(){
	// find project id
	// var project_id = $(this).val();
	// add this id to the hidden label
	// $('#p_hidden_id').html(project_id);

	// show confirm deletion popup
	$('#comment_delete_alert').modal('toggle');
});


$('#add_new_comment').click(function(){

	var csrftoken = $('#csrf_token').val();
	var comment = $('#comment_message_area').val(),
		commentedProjectID = $('#projectID_token').val();

    var requestJSON = {
		"project_id": commentedProjectID,
    	"content": comment,
        // "csrfmiddlewaretoken": csrftoken
    }

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajax({
        url: window.SERVER_PATH + "projects/" + commentedProjectID + "/comment/add/",
        type: "POST",
        data: JSON.stringify(requestJSON),
        contentType: "application/json",
        success: function(data){
            console.log(data);
            // if(data['status'] == 'success') {
            //     window.location = window.SERVER_PATH + "projects/plist/";
            // }
        },
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });	

});