document.getElementById('totalTip').style.display = 'none';
var button = document.getElementById('calculate');
button.addEventListener('click' , calculateTip);

function calculateTip () {
	var billAmt = document.getElementById('billamt').value;
	var serviceQual  = document.getElementById('serviceQual').value;
	var numOfPeople = document.getElementById('peopleamt').value;

	if (serviceQual == 0 || billAmt == '') {
		alert("You must enter all values");
		return;
	}
	if (numOfPeople == "" || numOfPeople<1) {
		numOfPeople = 1;
		document.getElementById('each').style.display = 'none';
	}
	else {
		document.getElementById('each').style.display = 'block';
	}

	var total = (billAmt*serviceQual/numOfPeople).toFixed(2);
	console.log(total);

	document.getElementById('totalTip').style.display = 'block';
	document.getElementById('tip').innerText = total;
	document.getElementById('tip').style.display = 'block';
}
