/*
var stringList = ["Hello", "World", "in", "a", "frame"];
var star = "*";

var longLen = findLongest(stringList);
console.log("longLen: " +longLen);

function findLongest (thing) {
	var longest = 0;
	for (var i=0; i<thing.length; i++) {
		if (thing[i].length > longest) {
			longest = thing[i].length;
		}
		console.log("longest: " +longest);
	}
	return longest;
}


var boxWidth = longLen+4;
var boxHeight = stringList.length+2;

var space = " ";
function updateWords (sList) {
	for (i=0; i<sList.length; i++) {
		if (sList[i].length<longLen) {
			sList[i] = 
		}
	}
}
*/





//notes from Jonathan: 

let sentence = prompt("Enter a sentence: ");
let words = sentence.split(" ");
//split sentence to array

let longest_length = get_longest_word_length(words);
let border = Array(longest_length+4).fill("*").join("");
// creates array, fills it with *'s, then joins it to be a string
// will be used for top and bottom border

border = border + "\n";
// "\n" is like <br>

let middle_stuff = "";
for (current_word of words) {
	middle_stuff = middle_stuff+ "* " +current_word + Array(longest_length - current_word.length).fill(" ").join("") + " *" + "\n";
}
//on a new line every time, prints star, space, the word, fills the rest of the space and ends with a *



let answer = border + middle_stuff +border;
console.log(answer);



function get_longest_word_length (words) {	
	let longest_length = 0;
	for (current_word of words) {
		if (current_word.length > longest_length) {
			longest_length = current_word.length;
		}
	}
	return longest_length;
}