// 1
var array = ["Banana", "Apples", "Oranges", "Blueberries"];

array.shift();

array.sort();

array.push("Kiwi");

array.shift();

array.reverse();
console.log(array);


// 2
var arr = ["Banana", ["Apples", ["oranges"], "Blueberries"]];
var x = arr[1][1][0];
console.log(x);


//3

var obj = {
	username: "someUser",
	password: "somePassword"
};

var database = [obj];



var obj1 = {
	username:1, timeline:1
};
var obj2 = {
	username:2, timeline:2
};
var obj3 = {
	username:3, timeline:3
};

var newsfeed = [obj1, obj2, obj3];
console.log(newsfeed);


// 4

function mult (x,y) {
	var math = x*y;
	return math;
}

console.log("My age is "+mult(5,9));


//is the same as:

var multiply = function(x,y) {
	return x*y;
}

console.log("My age is "+multiply(4,9));

//is also the same as:

var multiplication = (x, y) => (x*y);
console.log("My age is "+multiplication(3,9));


//5

const gender = (personGender) => {
	if (personGender == "female") {
		console.log("You are female")
	}
	else {
		console.log("You are male")
	}
}

gender("male")