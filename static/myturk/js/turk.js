
$('.selectpicker').selectpicker();

// refresh the data view when changing selected dataset
$('.selectpicker').on('change', function(){
    requestDataset($('.selectpicker').selectpicker('val'));

});

/*
* show the content of a certain dataset
* @param datasetId, the ID of a dataset
*/
function requestDataset(datasetId){
    // cancel ajax to get values from all inputs
    $.ajaxSetup({async:false});
    var csrftoken = $('#csrf_token').val();
    
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajax({
        url: window.SERVER_PATH + "datasets/load_doc_data/",
        type: "POST",
        data: JSON.stringify({'dataset_id': datasetId}),
        contentType: "application/json",
        success: function(data){
            console.log(data);
            if(data['status'] == 'success') {
                // delete the previous table
                $('#data_view').dataTable().fnDestroy();
                // initialize the table
                $('#data_view').dataTable( {
                    "data": data['docs'],
                    "bLengthChange": false,
                    "paging": true,
                    "info": true,
                    "bFilter": false, //Disable search function
                    "columns": [
                        { "data": "doc_id", "width": "8%" },
                        { "data": "doc_text", "orderable": false }
                    ]
                });
            }
        },
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });	
}

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
