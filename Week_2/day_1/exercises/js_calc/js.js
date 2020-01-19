//Third try

let numbers = [];
let currentVal = '';
let sign = '';
let answer;


function store_num(x) {
	if (x>=0 && x<=9) {
		currentVal=currentVal+x;
		console.log(currentVal);
	}
	else if (x != '=') {
		numbers.push(currentVal);
		sign = x;
		currentVal='';
	}
	else {
		numbers.push(currentVal);
		num1 = Number(numbers[0]);
		num2 = Number(numbers[1]);
		switch (sign) {
			case '-':
			answer = num1-num2;
			alert(answer);
			break;
			case '/':
			answer = num1/num2;
			alert(answer);
			break;
			case '+':
			answer = num1+num2;
			alert(answer)
		}
		currentVal='';
		sign = '';
		numbers = [];
	}
}









// First try

// let currentVal='';
// let secondVal='';
// let holder=0;
// let divideHolder=1;

// function my_f(x) {
// 	if (x>=0 && x<=9) {
// 		currentVal=currentVal+x;
// 		console.log(currentVal);
// 	}
// 	else {
// 		currentVal = Number(currentVal);
// 		console.log(currentVal);
// 		if (x == '+') {
// 			currentVal = currentVal+holder;
// 			function my_f(x) {
// 				if (x>=0 && x<=9) {
// 					secondVal=secondVal+x;
// 					console.log(secondVal);
// 				}
// 				else {
// 					holder = secondVal;
// 					alert(currentVal);
// 				}
// 			}
// 		}
// 		else if (x == '-') {
// 			currentVal = currentVal-holder;
// 			function my_f(x) {
// 				if (x>=0 && x<=9) {
// 					secondVal=secondVal+x;
// 					console.log(secondVal);
// 				}
// 				else {
// 					holder = secondVal;
// 					alert(currentVal);
// 				}
// 			}
// 		}
// 		else if (x == '/') {
// 			currentVal = currentVal/divideHolder;
// 			function my_f(x) {
// 				if (x>=0 && x<=9) {
// 					secondVal=secondVal+x;
// 					console.log(secondVal);
// 				}
// 				else {
// 					divideHolder = secondVal;
// 					alert(currentVal);
// 				}
// 			}
// 		}
// 	}
// }






// Second try

// let input = "";
// let num1 = 0;
// let num2 = 0;
// let sign = "";



// function my_f(x) {
// 	if (x>=0 && x<=9) {
// 		input=input+x;
// 		console.log(input);
// 	}
// 	else {
// 		num1 = parseInt(input);
// 		console.log(num1);
// 	}
// }

// function my_f(x) {
// 	if (x=='+') {
// 		sign = '+';
// 		console.log(sign);
// 	}
// 	else if (x=='-') {
// 		sign = '-';
// 		console.log(sign);
// 	}
// 	else if (x=='/') {
// 		sign = '/';
// 		console.log(sign);
// 	}
// }

// function my_f(x) {

// }