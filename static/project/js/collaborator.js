
// remove a collaborator
$('.remove_collaborators').click(function() {

	var selectedColID = $(this).prop('title');
	// remove the selected collaborator (front end)
	$('#' + selectedColID).remove();
})


$('#btn_collaborator_add').click(function(){
	console.log('add');
	$('#list_collaborator').prepend('<li class="list-group-item" id="col_list_id"><div class="row"><div class="col-xs-3 col-md-2 left_15_gap"><img src="' + window.PUBLIC_PATH + 'common/imgs/default.jpg" class="img-circle img-responsive" alt="" /></div></div></li>');
})