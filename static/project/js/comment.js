
// add a new comment
$('#add_new_comment').click(function(){

	var csrftoken = $('#csrf_token').val();
	var comment = $('#comment_message_area').val(),
		commentedProjectID = $('#projectID_token').val();

    var requestJSON = {
		"project_id": commentedProjectID,
    	"content": comment
    }

    commentUpdateRequest('add', requestJSON, csrftoken);	
});


var commentIDForDelete = '';
// show popup for confirming deletion
$('.btn_comment_delete').on('click', function(){
    // show confirm deletion popup
    $('#comment_delete_alert').modal('toggle');
    commentIDForDelete = $(this).val();
});

// delete a comment
$('#btn_comment_delete_confirm').click(function(){
    var csrftoken = $('#csrf_token').val();
    var commentedProjectID = $('#projectID_token').val();

    var requestJSON = {
        "project_id": commentedProjectID,
        "comment_id": commentIDForDelete
    }

    commentUpdateRequest('delete', requestJSON, csrftoken);               
});


// edit a comment
$('.btn_comment_edit').click(function(){
    // cancel ajax
    $.ajaxSetup({async:false}); 
    var commentID = $(this).val(),
        commentContent = $('#comment_content_' + commentID).html().toString();

    console.log(commentContent);

    $('#comment_edit_area_' + commentID).html(commentContent); 

    $('#comment_content_' + commentID).addClass('hide_this');
    $('#comment_edit_' + commentID).removeClass('hide_this');

});



function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

/*
* Refresh the comment list
* @param commentListID, ID of the comment list
* @param Comments, the array of comments
*/
function refreshCommentList(commentListID, comments) {
    // cancel ajax
    $.ajaxSetup({async:false});   
    // empty the list
    $(commentListID).empty();

    for (var i = 0; i < comments.length; i++) {
        var commentInfoStart = '<li class="list-group-item">' + 
                                    '<div class="row">' + 
                                        '<div class="col-xs-3 col-md-1 left_15_gap">' + 
                                            '<img src="' + window.PUBLIC_PATH + 'common/imgs/default1.png" class="img-circle img-responsive" alt="" />'+ 
                                        '</div>' +
                                        '<div class="col-xs-7 col-md-10">'+ 
                                            '<div class="col-md-10">'+ 
                                                '<div class="mic-info">'+ 
                                                    'By: <a href="#">' + comments[i]['user'] + '</a> On ' + comments[i]['pub_date']+  
                                                '</div>'+
                                                '<div class="comment-text">'+ 
                                                    '<p>' + comments[i]['content'] + '</p>'+ 
                                                '</div>'+                                          
                                            '</div>';

        var btnEditDel = '<div class="col-md-2 col-md-offset-0">'+ 
                            '<button type="button" class="btn btn-primary btn-xs btn_comment_edit" title="Edit" value="' + comments[i]['comment_id'] + '">'+ 
                                '<span class="glyphicon glyphicon-pencil"></span>'+
                            '</button>'+ 
                            '<button type="button" class="btn btn-danger btn-xs btn_comment_delete btn_appended" title="Delete" value="' + comments[i]['comment_id'] + '">'+ 
                                '<span class="glyphicon glyphicon-remove"></span>'+
                            '</button>'+
                        '</div>';

        var btnDel = '<div class="col-md-2 col-md-offset-0">'+
                            '<button type="button" class="btn btn-danger btn-xs btn_comment_delete btn_appended" title="Delete" value="' + comments[i]['comment_id'] + '">'+ 
                                '<span class="glyphicon glyphicon-remove"></span>'+
                            '</button>'+
                        '</div>';

        var commentInfoEnd = '</div>'+
                        '</div>'+ 
                    '</li>';                                   

        // with edit and delete button
        if (comments[i]['edit_enable'] == true)
            $(commentListID).append(commentInfoStart + btnEditDel + commentInfoEnd);
        // just delete
        else if (comments[i]['edit_enable'] == false && comments[i]['edit_enable'] == true)
            $(commentListID).append(commentInfoStart + btnDel + commentInfoEnd);
        // no edit or delete
        else if (comments[i]['edit_enable'] == false && comments[i]['edit_enable'] == false)
            $(commentListID).append(commentInfoStart + commentInfoEnd);
             
    }

    // update the comment number
    $('#comlist_num').html(comments.length);

    // show popup for confirming deletion
    $('.btn_comment_delete').on('click', function(){
        // show confirm deletion popup
        $('#comment_delete_alert').modal('toggle');
        commentIDForDelete = $(this).val();
    });   
}


function commentUpdateRequest(type, request, csrftoken) {
    $.ajax({
        url: window.SERVER_PATH + 'projects/comment/' + type + '/',
        type: "POST",
        data: JSON.stringify(request),
        contentType: "application/json",
        success: function(data){
            if(data['status'] == 'success') {
                refreshCommentList('#comment_list', data['comments']);
            }
            if (type == 'delete')
                $('#comment_delete_alert').modal('hide');
        },
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
}