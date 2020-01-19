// // alert('hey there');

// // console.log('hello from log');

// console.log(1+1);

// console.log('hello' + ' ' + 'world')

// var x = 1;

// var y = 2;

// console.log(x+y);

// let a = 5;
// // 'let' replaces 'var' in the new js for assigning
// // variables

// console.log(a);


// const b = 9;
// // with 'const' once declared, cannot be redefined


// if (1==2) {
// 	console.log('true');
// }
// else {
// 	console.log('not true');
// }




// let z = 'main';

// switch (z) {
// 	case 'home':
// 	console.log('home');
// 	break;
// 	case 'main':
// 	console.log('haha');
// 	break;
// 	default:
// 	console.log(':(');
// }



// //methods:

// toString();
// // creates string

// toFixed();
// var x = 9.656;

// x.toFixed(0);  //returns 10
// x.toFixed(2);  //returns 9.66
// x.toFixed(4);  //returns 9.66



// Number Methods

// toString()

// var x = 123;
// x.toString();            // returns 123 from variable x
// (123).toString();        // returns 123 from literal 123
// (100 + 23).toString();   // returns 123 from expression 100 + 23


// toFixed()
// var x = 9.656;
// x.toFixed(0);           // returns 10
// x.toFixed(2);           // returns 9.66
// x.toFixed(4);           // returns 9.6560
// x.toFixed(6);           // returns 9.656000

// toPrecision()
// var x = 9.656;
// x.toPrecision();        // returns 9.656
// x.toPrecision(2);       // returns 9.7
// x.toPrecision(4);       // returns 9.656
// x.toPrecision(6);       // returns 9.65600


// Number()
// parseInt()
// parseFloat()

// Number()	Returns a number, converted from its argument.
// parseFloat()	Parses its argument and returns a floating point number
// parseInt()	Parses its argument and returns an integer

// Number(true);          // returns 1
// Number(false);         // returns 0
// Number("10");          // returns 10
// Number("  10");        // returns 10
// Number("10  ");        // returns 10
// Number(" 10  ");       // returns 10
// Number("10.33");       // returns 10.33
// Number("10,330");       // returns NaN
// Number("10 33");       // returns NaN
// Number("John");        // returns NaN

// parseInt("10");         // returns 10
// parseInt("10.33");      // returns 10
// parseInt("10 20 30");   // returns 10
// parseInt("10 years");   // returns 10
// parseInt("years 10");   // returns NaN

// parseFloat("10");        // returns 10
// parseFloat("10.33");     // returns 10.33
// parseFloat("10 20 30");  // returns 10
// parseFloat("10 years");  // returns 10
// parseFloat("years 10");  // returns NaN



// // // Strings method
// var txt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
// var a = txt.length;
// //
// // //
// var str = "Please locate where 'locate' occurs!";
// var pos = str.indexOf("locate");
// // //
// console.log(pos);
// // //
// // // var str = "Please locate where 'locate' occurs!";
// // // var pos = str.lastIndexOf("locate");
// // // console.log(pos);
// // // //
// // // var str = "Please locate where 'locate' occurs!";
// // // var pos = str.indexOf("locate);
// // // //
// // var str = "Please locate where 'locate' occurs!";
// // var pos = str.search("locate");
// // // console.log(pos);
// // // // slice(start, end)
// // // // substring(start, end)
// // // // substr(start, length)
// // // //
// // var str = "Apple, Banana, Kiwi";
// // var res = str.slice(7, 13);
// // console.log(res);
// //
// // var str = "Apple, Banana, Kiwi";
// // var res = str.slice(-12, -6);
// // // //
// // // // var res = str.slice(7);
// // // // var res = str.slice(-12);
// // // //
// // var str = "Apple, Banana, Kiwi";
// // var res = str.substring(7, 13);
// // var res = str.substring(7);
// // console.log();
// //
// // var str = "Apple, Banana, Kiwi";
// // var res = str.substr(7);
// // var res = str.substr(-4);
// //
// // str = "Please visit Microsoft!";
// // var n = str.replace("Microsoft", "Developers Institute");
// // var n = str.replace("MICROSOFT", "Developers Institute");
// // // //
// // var text1 = "Hello World!";       // String
// // var text2 = text1.toUpperCase();
// // var text2 = text1.toLowerCase();
// //
// // var text1 = "Hello";
// // var text2 = "World";
// // var text4 = "FAin";
// // var text3 = text1.concat(" ", text2, text4);
// // console.log("text3",text3);
// // //
// // var str = "       Hello World!        ";
// // str = str.trim();
// // console.log(str);
// // //
// var str = "HELLO WORLD";
// str.charAt(0);

// // //
// var str = "hELLO WORLD";
// str.charCodeAt(0)
// console.log("charCodeAt",str.charCodeAt(0));
// // //
// var str = "HELLO WORLD";
// str[0];
// // //
// // //
// // console.log();




// let param1 = prompt('This is the prompt message')
// console.log(param1);


let param1 = prompt('Enter a number')
console.log(param1);

let param2 = prompt('Choose + or -')
console.log(param2);

let param3 = prompt('Enter another number')
console.log(param3);

var x;

// if (param2 === '+') {
// 	x = Number(param1) + Number(param3);
// 	alert(param1 + " " + param2 + " " + param3 + " " + '=' + " " + x);
// }

// else if (param2 === '-') {
// 	x = Number(param1) - Number(param3);
// 	alert(param1 + " " + param2 + " " + param3 + " " + '=' + " " + x);
// }

// else {
// 	alert('You did not enter the correct parameters')
// }



switch (param2) {
	case '-':
	x = Number(param1) - Number(param2);
	alert(param1 + " " + param2 + " " + param3 + " " + '=' + " " + x);
	break;
	case '+':
	x = Number(param1) + Number(param2);
	alert(param1 + " " + param2 + " " + param3 + " " + '=' + " " + x);
	break;
	default:
	alert('You must choose + or -')
}






// function nameOfFunction() {
// 	alert('Ha ha , alert from my function');
// }
// defines function

// nameOfFunction();
// calls function