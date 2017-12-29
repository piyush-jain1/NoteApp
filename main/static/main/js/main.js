/* Signup Form AJAX */
$('#signupForm').submit(function(e){
	var formId = $(this).attr('id');
	var submitBtn = $(this).find('input[type=submit]');
	$('#user-phone-exists-error').css('display','none');
	$('#user-email-exists-error').css('display','none');
	submitBtn.prop('disabled', true);
	e.preventDefault();
	$.ajax({
		url: "/user/signup", // the file to call
		type: "POST", // G2+4POST
		data: $(this).serialize(), // get the form data
		success: function(data){
			var signup_response = jQuery.parseJSON(data);
			if (signup_response.register == "Success") {
				$('#register-modal').modal('hide');
				submitBtn.prop('disabled', false);
			}
			else if (signup_response.register == "Failure_email") {
				$('#user-email-exists-error').css('display','block');
				submitBtn.prop('disabled', false);
			}
			else if (signup_response.register == "Failure_phone") {
			    $('#user-phone-exists-error').css('display','block');
				submitBtn.prop('disabled', false);
			}
			else if(signup_response.error == "True") {
                $('#register-modal').modal('hide');
                setTimeout(function () {
                    $('#errorModal').modal({backdrop: 'static', keyboard: false, show: true});
                }, 1000);
            }
		},/* end of Success */
		error: function(data) {
			$('#register-modal').modal('hide');
			setTimeout(function() {
				$('#errorModal').modal({backdrop:'static', keyboard:false,show:true});
			}, 1000);
		}/*  end of error */
	});/*./ajax*/
    var form = document.getElementById(formId);
    form.reset();
});
/* End of Signup Form */

/* Login form AJAX */
$('#loginform').submit(function(e){
	var formId = $(this).attr('id');
	var submitBtn = $(this).find('input[type=submit]');
	$('#no-user-error').css('display', 'none');
    $('#password-error').css('display', 'none');
    submitBtn.prop('disabled', true);
    e.preventDefault();
	$.ajax({
		url: "/user/login", // the file to call
		type: "POST", // GET or POST
		data: $(this).serialize(), // get the form data
        success: function(data) {
            var login_response = jQuery.parseJSON(data);
            // alert("nvjndvv");
            // console.log(login_response);
            if (login_response.user == "nouser") {
                $('#no-user-error').css('display', 'block');
                submitBtn.prop('disabled', false);
            }
            else if (login_response.user == "password wrong") {
                $('#password-error').css('display', 'block');
                submitBtn.prop('disabled', false);
            }
            else {
                if (login_response.login == "Success") {
                    document.getElementById(formId).reset();
                    $('#login-modal').modal('hide');
                    setTimeout(function() {
                    window.location = 'http://www.example.com?username=' + login_response.username;
                    }, 400);
                }
                else {
                    alert("Invalid Login!");
                }
                /*./else*/
                submitBtn.prop('disabled', false);
                $('#spinner-login').css('display', 'none');
            }
            /* end of Success */
        },
		error: function(data) {
			$('#loginModal').modal('hide');
			$('#errorModal').modal({backdrop:'static', keyboard:false,show:true});
		}/*  end of error */
	});/*./ajax*/
	document.getElementById(formId).reset();
});
/*End of loin form AJAX */

$('#login').click(function(){
$('#login-modal').modal('show');
});

$('#signup').click(function(){
$('#register-modal').modal('show');
});
