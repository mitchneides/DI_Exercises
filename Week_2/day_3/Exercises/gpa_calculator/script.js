// var userGrade = [];
// var userCoefficient = [];

// var grade = prompt("Enter a grade: ");
// userGrade.push(grade);

// var coefficient = prompt("Enter a coefficient: ");
// userCoefficient.push(coefficient);

// var average = (grade*coefficient)/(userGrade.length);

// if (average == 0) {
// 	if (userGrade[0] == "" || userGrade.length == 0) {
// 	grade = prompt("You must enter a grade: ");
// 	userGrade.push(grade);
// 	userGrade.shift();
// 	}
// 	if (userCoefficient[0] == "" || userCoefficient.length == 0) {
// 	coefficient = prompt("You must enter a coefficient: ");
// 	userCoefficient.push(coefficient);
// 	}
// 	average = (grade*coefficient)/(userGrade.length);
// 	alert("The average is "+average);
// }
// else {
// 	alert("The average is "+average);
// }

var subject;
var grade;
var credHours;
var anotherClass = true;
var gpa;

var classSubjects = [];
var gradeScores = [];
var classHours = [];
var totalScore = 0;
var totalHours = 0;


while (anotherClass == true) {
	subject = prompt("Enter a class: ");
	while (emptyCheck(subject) == true) {
		subject = prompt("You must enter a class: ");
	}
	classSubjects.push(subject);
	console.log(classSubjects);
	//takes course subject, adds to array classSubjects

	grade = prompt("Enter your grade (a , b , c , d , f) for " +subject +": ");
	while (emptyCheck(grade) == true) {
		grade = '';
		grade = prompt("You must enter a grade (a , b , c , d , f): ");
	}
	while ((grade != 'a') && (grade != 'b') && (grade != 'c') && (grade != 'd') && (grade != 'f')) {
		grade = prompt("Your grade must be: a , b , c , d or f. Enter your grade (a , b , c , d , f) for " +subject +": ");
	}
	switch (grade) {
		case "a":
		gradeScores.push(4);
		break;
		case "b":
		gradeScores.push(3);
		break;
		case "c":
		gradeScores.push(2);
		break;
		case "d":
		gradeScores.push(1);
		break;
		case "f":
		gradeScores.push(0);
		break;
	}
	console.log(gradeScores);
	//takes course grade, checks that it is valid,
	//converts to grade scale (number) value, 
	//adds to array gradeScores 

	credHours = prompt("Enter the number of credit hours for " +subject +": ");
	while (emptyCheck(credHours) == true) {
		credHours = prompt("You must enter the number of credit hours for " +subject +": ");
	}
	classHours.push(credHours);
	totalHours = totalHours+Number(credHours);
	console.log("Total hours is now: " +totalHours);
	//takes hours for course, adds to totalHours

	let again = prompt("Would you like to add another class? Enter y for yes, n for no: ");
	if (again == 'y') {
		anotherClass = true;
	}
	else {
		anotherClass = false;
	}
}

for (i=0; i<classSubjects.length; i++) {
	let times = gradeScores[i]*classHours[i];
	totalScore = totalScore+times;
}


gpa = totalScore/totalHours;
gpa = (Math.round(gpa * 100) / 100).toFixed(2);
console.log("User GPA: " +gpa);
alert("Your GPA is: " +gpa);
// calculates final GPA



function emptyCheck(x) {
	if (x == "") {
		return true;
	}
	else {
		return false;
	}
}
