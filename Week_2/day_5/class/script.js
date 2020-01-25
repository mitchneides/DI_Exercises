/*

// write a function that checks if something is a character

function isChar(chr) {
	if (chr.length>1) {
		return 'Enter a valid char';
	}
	let str = 'abcdefghijklmnopqrstuvwxyz';
	for(let i = 0; i<str.length; i++) {
		if (chr.toLowerCase() == str[i]) {
			return true;
		}
	}
	return false;
}
let is_char = isChar('R');
console.log(is_char);



// ternary operator:

let x = (1===1) ? 10 : 1;
// if 1===1 then x=10, else x=1
	//returns 10




const x = (a, b, c) => {}
//arrow function

// ie:
var hello;
hello = (val) => "Hello " + val;
// function hellp takes a value and outputs "Hello" + the value that was put in
console.log(hello("Universe!"));
// returns Hello Universe!





//forEach is only for arrays

//Object.keys().forEach turns object into an array and then forEach can be used

Object.entries(obj).forEach( item => {
	//instructions
})


try {
	console.log("Before");
	x
}
catch (err) {
	console.log(err);
}
finally {
	console.log("no matter what, this will run");
}
console.log("after");

*/


var word = 'hello' //want "Hello"

var newWord = word.substring(0,1).toUpperCase() + word.substring(1,5);
console.log(newWord);

//or

newAgain = word.charAt(0).toUpperCase() + word.slice(1);
console.log(newAgain);



