
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

    $('#comment_list').prepend('<li class="list-group-item"><div class="row"><div class="col-xs-4 col-md-2 left_15_gap"><img src="' + window.PUBLIC_PATH + 'common/imgs/default1.png" class="img-circle img-responsive" alt="" /></div><div class="col-xs-7 col-md-9"><div><a href="#" target="_blank">Placeholder for Comment Topics</a><div class="mic-info"><p>By: <a href="#"> A FAKE USER</a> on TODYA </p></div></div><div class="comment-text">'+ comment +'</div><div class="action"><button type="button" class="btn btn-primary btn-xs" title="Edit"><span class="glyphicon glyphicon-pencil"></span></button><button type="button" class="btn btn-danger btn-xs btn_comment_delete" title="Delete"><span class="glyphicon glyphicon-remove"></span></button></div></div></div></li>');

    // function csrfSafeMethod(method) {
    //     // these HTTP methods do not require CSRF protection
    //     return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    // }

    // $.ajax({
    //     url: window.SERVER_PATH + "projects/" + commentedProjectID + "/comment/add/",
    //     type: "POST",
    //     data: JSON.stringify(requestJSON),
    //     contentType: "application/json",
    //     success: function(data){
    //         console.log(data);
    //         // if(data['status'] == 'success') {
    //         //     window.location = window.SERVER_PATH + "projects/plist/";
    //         // }
    //     },
    //     beforeSend: function(xhr, settings) {
    //         if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
    //             xhr.setRequestHeader("X-CSRFToken", csrftoken);
    //         }
    //     }
    // });	

});