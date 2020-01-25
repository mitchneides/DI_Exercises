var bottles = prompt("Enter the number of bottles of beer on the wall: ");
var newBottles;

for (var count = 1; count<bottles ; count++) {
	console.log(bottles +" bottles of beer on the wall,");
	console.log(bottles +" bottles of beer.");
	console.log("Take " + count +" down, pass it around,");
	console.log(calcNewBottles());
	console.log("");
	bottles = newBottles;
	if (bottles == 1) {
		console.log("");
		console.log(bottles +" bottle of beer on the wall,");
		console.log(bottles +" bottle of beer.");
		console.log("Take " + bottles +" down, pass it around,");
		console.log("No more bottles of beer on the wall,");
	}
}

if (bottles != 1) {
	console.log(bottles +" bottles of beer on the wall,");
	console.log(bottles +" bottles of beer.");
	console.log("Take " + bottles +" down, pass it around,");
	console.log("No more bottles of beer on the wall,");
}


var str;
function calcNewBottles () {
	newBottles = bottles - count;
	if (newBottles == 1) {
		 str = "1 bottle of beer on the wall."
	}
	else {
		str = newBottles + " bottles of beer on the wall.";
	}
	return str;
}