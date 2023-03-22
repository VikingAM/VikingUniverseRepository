function saveNewPassword(){
	var name = $("#password_name").val();
	var category = $("#password_category").val();
	var username =  $("#password_username").val();
	var password = $("#new_password_management").val();
	var url = $("#password_url").val();
	var description = $("#new_password_description").val();

	$("#new_password_error").empty();
	$("#new_password_error").hide();
	if(inputCheckIfNotEmpty("password_name", "Password Name", "new_password_error") != true){ return false; }
	if(inputCheckIfNotEmpty("password_username", "Username / Email", "new_password_error") != true){ return false;}
	if(inputCheckIfNotEmpty("new_password_management", "Password", "new_password_error") != true){ return false;}
	if(inputCheckIfNotEmpty("password_url", "Url", "new_password_error") != true){return false;}
	$("#new_password_info_msg").show();
	$("#new_password_info_msg").append("Process request. . .");
	dataVal = {
		"csrfmiddlewaretoken": '{{ csrf_token }}',
        "userId": '{{ request.user.id }}',
        "category": category,
        "password_name":name ,
        "username": username,
        "password": password,
        "url": url,
        "description": description,
	}
	$.ajax({
        type: "POST",
        url: "{% url 'profileNewPassword' %}",
        data: dataVal,
        async:true,
        success: function (data) {
        	$("#new_password_info_msg").hide();
            if(data.status == 1){
            	$("#new_password_success_msg").show();
            	$("#new_password_success_msg").append(data.success_msg);
            	location.reload(true);
            }else{
            	$("#new_password_error").append(data.error_msg);
            	$("#new_password_error").show();
            }
        },
        error: function (e) {
            $("#new_password_error").append("Error! please try again later.");
        }
    })

}

function inputCheckIfNotEmpty(field_id, field_name, error_holder_field_name){
	var value = $("#"+field_id).val();
	if(value.length == 0){
		$("#"+field_id).focus();
		$("#"+error_holder_field_name).append(field_name+" Should not be empty!")
		$("#"+error_holder_field_name).show();
		return false;
	}else{
		return true;
	}
}

