let num1 = prompt("Enter a number: ");
let sign = prompt("Enter an operator (+ , - , * , /): ");
let num2 = prompt("Enter another number: ");
let solution;

switch (sign) {
	default:
	alert("Error: You did not enter a valid operator (+ , - , * , /)");
	break;
	case "+":
	solution = Number(num1)+Number(num2);
	alert(num1 +" + "+ num2+ " = "+ solution);
	break;
	case "-":
	solution = Number(num1)-Number(num2);
	alert(num1 +" - " +num2 +" = " +solution);
	break;
	case "*":
	solution = Number(num1)*Number(num2);
	alert(num1 +" * " +num2 +" = " +solution);
	break;
	case "/":
	solution = Number(num1)/Number(num2);
	alert(num1 +" / " +num2 +" = " +solution);
	break;
}