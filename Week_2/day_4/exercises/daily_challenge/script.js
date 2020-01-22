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

function updateRows (word) {
	
}