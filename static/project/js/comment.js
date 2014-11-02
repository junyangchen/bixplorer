
// add a new comment
$('#add_new_comment').click(function(){

	var csrftoken = $('#csrf_token').val();
	var comment = $('#comment_message_area').val(),
		commentedProjectID = $('#projectID_token').val();

    var requestJSON = {
		"project_id": commentedProjectID,
    	"content": comment
        // "csrfmiddlewaretoken": csrftoken
    }

    console.log(commentedProjectID);

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajax({
        url: window.SERVER_PATH + "projects/comment/add/",
        type: "POST",
        data: JSON.stringify(requestJSON),
        contentType: "application/json",
        success: function(data){
            console.log(data);
            // if(data['status'] == 'success') {
                // empty the list
                // $('#comment_list').empty();

                // for (var i = 0; i < data['comments'].length; i++) {

                //     // with edit and delete button
                //     if (data['comments'][i][5]['edit_enable'] == true)
                //         $('#comment_list').append('<li class="list-group-item"><div class="row"><div class="col-xs-4 col-md-2 left_15_gap"><img src="' + window.PUBLIC_PATH + 'common/imgs/default1.png" class="img-circle img-responsive" alt="" /></div><div class="col-xs-7 col-md-9"><div><a href="#" target="_blank">Placeholder for Comment Topics</a><div class="mic-info"><p>By: <a href="#"> ' + data['comments'][i][0]['user'] + '</a> on ' + data['comments'][i][4]['pub_date'] + ' </p></div></div><div class="comment-text">'+ data['comments'][i][1]['content'] +'</div><div class="action"><button type="button" class="btn btn-primary btn-xs btn_comment_edit" title="Edit" value="' + data['comments'][i][2]['comment_id'] + '"><span class="glyphicon glyphicon-pencil"></span></button><button type="button" class="btn btn-danger btn-xs btn_comment_delete" title="Delete" value="' + data['comments'][i][2]['comment_id'] + '"><span class="glyphicon glyphicon-remove"></span></button></div></div></div></li>');
                //     // without delete and edit button                    
                //     else
                //         $('#comment_list').append('<li class="list-group-item"><div class="row"><div class="col-xs-4 col-md-2 left_15_gap"><img src="' + window.PUBLIC_PATH + 'common/imgs/default1.png" class="img-circle img-responsive" alt="" /></div><div class="col-xs-7 col-md-9"><div><a href="#" target="_blank">Placeholder for Comment Topics</a><div class="mic-info"><p>By: <a href="#"> ' + data['comments'][i][0]['user'] + '</a> on ' + data['comments'][i][4]['pub_date'] + ' </p></div></div><div class="comment-text">'+ data['comments'][i][1]['content'] +'</div></div></div></li>');                   
                // }
            // }

            var el = $(' <li class="list-group-item">' + 
                                    '<div class="row">' + 
                                        '<div class="col-xs-3 col-md-1 left_15_gap">' + 
                                            '<img src="' + window.PUBLIC_PATH + 'common/imgs/default1.png" class="img-circle img-responsive" alt="" />' + 
                                        '</div>' + 

                                        '<div class="col-xs-7 col-md-10">' + 
                                            '<div class="col-md-10">' + 
                                                '<div class="mic-info">' + 
                                                    'By: <a href="#"> a fake user </a> on TODAY' + 
                                                '</div>' + 

                                                '<div class="comment-text">' + 
                                                    '<p>fake comment</p>' + 
                                                '</div>' +                                          
                                            '</div>' +
                                            '<div class="col-md-2 col-md-offset-0">' + 
                                                '<button type="button" class="btn btn-primary btn-xs btn_comment_edit" title="Edit" id="fake_btn">' + 
                                                    '<span class="glyphicon glyphicon-pencil"></span>'+
                                                '</button>' + 
                                            '</div>' +
                                        '</div>' +
                                    '</div>' + 
                                '</li>')

            //$('#comment_list').empty();
            $('#comment_list').html(el);

            // $('#comment_list').prepend('<li class="list-group-item"><div class="row"><div class="col-xs-4 col-md-2 left_15_gap"><img src="' + window.PUBLIC_PATH + 'common/imgs/default1.png" class="img-circle img-responsive" alt="" /></div><div class="col-xs-7 col-md-9"><div><a href="#" target="_blank">Placeholder for Comment Topics</a><div class="mic-info"><p>By: <a href="#"> A FAKE USER</a> on TODYA </p></div></div><div class="comment-text">'+ comment +'</div><div class="action"><button type="button" class="btn btn-primary btn-xs btn_comment_edit" title="Edit" value="13"><span class="glyphicon glyphicon-pencil"></span></button><button type="button" class="btn btn-danger btn-xs btn_comment_delete" title="Delete" value="13"><span class="glyphicon glyphicon-remove"></span></button></div></div></div></li>');
        },
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });	
});

$('#fake_btn').on('click', function(){
    alert("click!");
});

var commentIDForDelete = '';
// show popup for confirming deletion
$('.btn_comment_delete').on('click', function(){

    console.log('delete');

    // show confirm deletion popup
    $('#comment_delete_alert').modal('toggle');
    commentIDForDelete = $(this).val();
});


$('#btn_comment_delete_confirm').click(function(){
    var csrftoken = $('#csrf_token').val();
    var commentedProjectID = $('#projectID_token').val();

    var requestJSON = {
        "project_id": commentedProjectID,
        "comment_id": commentIDForDelete
    }

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajax({
        url: window.SERVER_PATH + "projects/comment/delete/",
        type: "POST",
        data: JSON.stringify(requestJSON),
        contentType: "application/json",
        success: function(data){
            console.log(data);
            // if(data['status'] == 'success') {
            //     window.location = window.SERVER_PATH + "projects/plist/";
            // }

            // hide the popup
            $('#comment_delete_alert').modal('hide');
            // remove the selected item
            $('#comment_list_' + commentIDForDelete).remove();

        },
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });                
});

$('.btn_comment_edit').click(function(){

    var commentID = $(this).val(),
        commentContent = $('#comment_content_' + commentID).html();

    console.log(commentContent);

    $('#comment_edit_area_' + commentID).html();   

    $('#comment_content_' + commentID).addClass('hide_this');
    $('#comment_edit_area_' + commentID).removeClass('hide_this');

})