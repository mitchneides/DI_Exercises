// // Exercise 1

// var me = ["my", "favorite", "color", "is", "blue"]

// console.log(me.join(" "));

// // Exercise 2

// let str1 = "hello";
// let str2 = "there";

// newStr(str1,str2);

// function newStr(x,y) {
// 	let end1 = str1.charAt((str1.length-1)); 
// 	let end2 = str2.charAt((str2.length-1));

// 	let start1 = str1.slice(0,(str1.length-1));
// 	let start2 = str2.slice(0,(str2.length-1));

// 	let final = start2+end1+" "+start1+end2;
// 	console.log(final);
// 	return final;
// }

// // Exercise 3

// let str = prompt("Enter a word: ");

// if (str.length<3) {
// 	alert("Your word, "+str+", has not been changed.");
// }
// else if (str.substring(((str.length)-3),str.length) == "ing") {
// 	alert("Your word has been changed to: " +str+"ly.");
// }
// else {
// 	alert("Your word has been changed to: " +str+"ing.");
// }


// Exercise 4

// str = "This movie is not so bad!";
// str = "This dinner is bad!";
let str = "This dinner is not that bad!";

let locNot;
let locBad;

findNot(str);
findBad(str);

function findNot (a) {
	locNot = a.indexOf("not");
	console.log(locNot);
	return locNot;
}

function findBad (a) {
	locBad = a.indexOf("bad");
	console.log(locBad);
	return locBad;
}


if (locNot==-1 || locBad==-1) {
	alert(str);
}
else if (locBad>locNot) {
	let first = str.substring(0,locNot);
	let newStr = first+ "good!";
	alert(newStr);
}