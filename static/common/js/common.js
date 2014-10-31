/*
* this file contains behavior for add view and edit view
*/

// show the defual dataset in the data view when loading the page
$(document).ready(function(){		
	
	// refresh the data view when changing selected dataset
	$('.selectpicker').on('change', function(){
		requestDataset($('.selectpicker').selectpicker('val'));
	});

	// Get the default dataset id
	var selected_dataset_id = $('.selectpicker').selectpicker('val');
	// display the content of the default dataset
	//requestDataset(selected_dataset_id);
});


// add a new project and save it in the add view
$("#new_project").ajaxForm(projectSave);

// Saving a project in the edit view
$("#save_project").ajaxForm(projectSave);

// clicking the cancel button and redirecting to the project list
$('#btn_edit_cancel').click(function(){
	window.location = window.SERVER_PATH + "project/plist/";
});

// restart a project
$('#btn_restart').click(function() {
	// delete the input for project name
	$('#project_name').val('');
	// delete the input for project description
	$('#project_des').val('');
	// reset the privacy to "yes"
	$(':radio[value="yes"]').prop('checked', true);
	// reset the dataset to be the 1st one
	if ($('#project_dataset option:selected').val() != $('#project_dataset option:first').val()) {
		console.log($('#project_dataset option:first').text());
		$('.selectpicker').selectpicker('val', $('#project_dataset option:first').val());
		$('.selectpicker').selectpicker('refresh');
	}
});


/*
* show the content of a certain dataset
* @param datasetId, the ID of a dataset
*/
function requestDataset(datasetId){
	$.post(window.SERVER_PATH + "project/load_doc_action/", {'dataset_id': datasetId}, function(data){
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
				{ "data": "doc_people", "orderable": false },
				{ "data": "doc_location", "orderable": false },
				{ "data": "doc_organization", "orderable": false },
				{ "data": "doc_phone", "orderable": false },
				{ "data": "doc_misc", "orderable": false }
			]
		});
	});
}


/*
* save the project into the database
*/
//var csrftoken = $.cookie('csrftoken');


function projectSave() {
    alert("test");
	// cancel ajax to get values from all inputs
    $.ajaxSetup({async:false});
    var csrftoken = $('#csrf_token').val();  

    // get all relevent information of a project
    var pid = $('#project_id').html(),
		pname = $('#project_name').val(),
    	pdes = $('#project_des').val(),
    	isPrivate = $(':radio:checked').val(),
		dataset = $('#project_dataset').selectpicker('val');

    var save_project = {
		"project_id": pid,
    	"project_name": pname,
    	"project_description": pdes,
    	"project_privacy": isPrivate,
    	"dataset_id": dataset
    }
    
	$.post(window.SERVER_PATH + "project/add/", save_project, function(data) {
		// redirect when the data has been stored in the database
		if(data.status == 'success') {
			window.location = window.SERVER_PATH + "project/plist/";
		}
    });	
}