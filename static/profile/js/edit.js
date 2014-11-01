
// add tooltip for first name
$('#edit_first_name').tooltip({
    html: "true",
    trigger: "focus",
    title: "<span id='first_name_msg' class='glyphicon glyphicon-remove' style=color:#FF0004;'></span> No empty first name",
	animation: false,
	placement: "bottom"
});
// show instance message
instMsgForText('#edit_first_name', '#first_name_msg');


// add tooltip for last name
$('#edit_last_name').tooltip({
    html: "true",
    trigger: "focus",
    title: "<span id='last_name_msg' class='glyphicon glyphicon-remove' style=color:#FF0004;'></span> No empty last name",
	animation: false,
	placement: "bottom"
});
// show instance message
instMsgForText('#edit_last_name', '#last_name_msg');



$('#btn_profile_edit').click(function(){
	// set first name
	$('#edit_first_name').val($('#profile_first_name').html());
	// set last name
	$('#edit_last_name').val($('#profile_last_name').html());
	// set email
	$('#edit_email').val($('#profile_email').html());
	// set location
	$('#edit_location').val($('#profile_location').html());	


	$('.hide_this').addClass('tmp_this')
	$('.hide_this').removeClass('hide_this');
	$('.active_this').addClass('hide_this');
});


// clicking event for the cancel button
$('#btn_profile_cancel').click(function(){
	// hide edit divs
	$('.tmp_this').addClass('hide_this');
	// display information divs
	$('.active_this').removeClass('hide_this');
	$('.hide_this').removeClass('tmp_this');

	// hide save button
	$('#btn_profile_save').addClass('hide_this');
	// hide cancel button
	$('#btn_profile_cancel').addClass('hide_this');
	// show edit button
	$('#btn_profile_edit').removeClass('hide_this');
});


/*
* Show wrong icon when validating fails
* @param msgID, the tooltip id 
*/
function valWrong(msgID) {
    $(msgID).removeClass("glyphicon-ok");
    $(msgID).addClass("glyphicon-remove");
    $(msgID).css("color","#FF0004");
}

/*
* Show success icon when validating fails
* @param msgID, the tooltip id 
*/
function valCorrect(msgID) {
    $(msgID).removeClass("glyphicon-remove");
    $(msgID).addClass("glyphicon-ok");
    $(msgID).css("color","#00A41E");

    // hide the alert
    if (!$('#alert_msg').hasClass('hide_this'))
    	$('#alert_msg').addClass('hide_this');
}

/*
* Show instance message for text input box
* @param inputTextID, the text input box id
* @param msgID, the tooltiop id 
*/
function instMsgForText(inputTextID, msgID) {
	$(inputTextID).on('shown.bs.tooltip', function(){
		// check when the input value changes
		$(inputTextID).keyup(function(){
			if ($(inputTextID).val().length > 0)
				valCorrect(msgID);
			else
				valWrong(msgID);		
		});
		// check when user clicking the input box
		$(inputTextID).click(function(){
			if ($(inputTextID).val().length > 0)
				valCorrect(msgID);
			else
				valWrong(msgID);		
		});
	});	
}