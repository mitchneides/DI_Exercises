var body = document.getElementById('body');

var input = document.createElement("input");
input.setAttribute('type','text');
input.setAttribute('id', 'input');
input.setAttribute('placeholder','enter your email');
body.append(input);

var button = document.createElement('button');
button.innerText = "Submit";
button.style.marginLeft = '5px';
body.append(button);

button.addEventListener('click', function(e) {
	var email = document.getElementById('input');
	console.log(email.value);
	validate(email.value);
})

input.addEventListener('keypress', function(e) {
	if (e.keyCode == 13) {
		var email = document.getElementById('input');
		console.log(email.value);
		validate(email.value);
	};
})

function validate(email) {
	if(email.trim().length == 0) {
		alert("Enter a valid email");
	}
	else if (email.includes('@') == false || email.includes('.co') == false) {
		alert("Enter a valid email");
	}
	else {
		alert("Your email is: " +email);
	}
}
