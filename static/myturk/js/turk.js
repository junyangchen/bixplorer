
$('.selectpicker').selectpicker();

$('#btn_submit_turk').click(function(){


    var csrftoken = $('#csrf_token').val();
    var projectID = $('#projectID_token').val();

    var requestJSON = {
        "project_id": projectID,
        "collaborator_name": colName
    } 

    $.ajax({
        url: window.SERVER_PATH + 'myturk/createhit/',
        type: "POST",
        data: JSON.stringify(requestJSON),
        contentType: "application/json",
        success: function(data){
            if(data['status'] == 'success') {
            	console.log('success!');
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



var table = $('#example').DataTable();
 
    $('#example tbody').on( 'click', 'tr', function () {
        $(this).toggleClass('selected');
    } );
 
    $('#button').click( function () {
        alert( table.rows('.selected').data().length +' row(s) selected' );
    } );
