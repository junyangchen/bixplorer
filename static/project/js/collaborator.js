
// remove a collaborator
$('.remove_collaborators').click(function() {

	var selectedColID = $(this).prop('title');
	// remove the selected collaborator (front end)
	$('#' + selectedColID).remove();
})
