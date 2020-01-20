// Exercise 1

let num;
getNum();
checkEven(num);

function getNum() {
	num = prompt("Enter a number: ");
	console.log(num);
	return num;
}

function checkEven(num) {
	if (num % 2 == 0) {
		alert(num + " is an even number.");
	}
	else {
		alert(num + " is an odd number.");
	}
}


// Exercise 2

let x=13;
let y=9;

if (x>y) {
	console.log(x + " is greater than " + y);
}
else {
	console.log(y + " is greater than " + x);
}


// Exercise 3

let lang = prompt("Enter your native language: ");
console.log(lang);

if (lang == "French" || lang == "french") {
	alert("Bonjour");
}
else if (lang == "English" || lang == "english") {
	alert("Hello");
}
else if (lang == "Hebrew" || lang == "hebrew") {
	alert("Shalom");
}
else {
	alert(":)");
}



// Exercise 4

let grade = prompt("Enter your grade: ");
console.log(grade);
if (grade == 100) {
	console.log("A");
}
else if (grade.length<2) {
	grade = 0+grade;
	let compGrade = grade.charAt(0);
	switch (compGrade) {
		default:
			console.log("D");
			break;
		case '9':
			console.log("A");
			break;
		case '8':
			console.log("B");
			break;
		case '7':
			console.log("C");
			break;
	}
}
else {
	let compGrade = grade.charAt(0);
	switch (compGrade) {
		default:
			console.log("D");
			break;
		case '9':
			console.log("A");
			break;
		case '8':
			console.log("B");
			break;
		case '7':
			console.log("C");
			break;
	}
}
