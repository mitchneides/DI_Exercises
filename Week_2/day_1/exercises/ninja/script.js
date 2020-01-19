let str = getStr();
let editable = bigenough(str);
let ending = checkEnd(editable);


function getStr(){
	return prompt("Enter a string: ")
}

function bigenough(str) {
	if (str.length>=3) {
		return true;
	}
	else {
		console.log("Your word, " + str + ", has not been changed.");
	}
}

function checkEnd(editable) {
	if (editable==true) {
		var lastThree = str.substring(str.length - 3, str.length);
		if (lastThree === 'ing') {
			console.log("Your word is now: " + str + "ly");
		}
		else {
			console.log("Your word is now: " + str + "ing");
		}
	}
}