var min = 0;
var max = 1000;
var guess;
var needs_higher = true;
var continue_playing = true;
var guesses = 0;

alert("Let's play a game." + "\n" + "Think of a number between 1 and 1000." + "\n" + "I bet I can guess it in less that 10 guesses.");
while (continue_playing == true) {
	make_guesses();
}
alert("Nice! It only took me " +guesses + " guesses.")

function cpu_guess (min, max) {
	guess = Math.round((max+min) / 2);
	return guess;
}

function make_guesses() {
	var info = prompt("My guess is " + cpu_guess(min,max) + "\n" + "Respond H if your number is higher, L if it is lower, or C if I am correct.");
	switch (info) {
		case "H":
			needs_higher = true;
			break;
		case "L":
			needs_higher = false;
			break;
		case "C":
			continue_playing = false;
			break;
	}
	update_max_and_min();
	guesses++;
}

function update_max_and_min () {
	if (needs_higher == true) {
		min = guess;
	}
	else {
		max = guess;
	}
}