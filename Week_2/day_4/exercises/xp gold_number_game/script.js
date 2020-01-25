function playTheGame () {
	var c = confirm("Would you like to play the game?");
	if (c == true){
		var num = prompt("Great! Enter a number between 0 and 10.");
		if (num == "") {
			alert("Sorry, that's not a number. Goodbye");
			return;
		}
		else if(num<0 || num>10) {
			alert("Sorry, that's not in range. Goodbye");
			return;
		}
		else if(isNaN(num) == true) {
			alert("Sorry, that's not a number. Goodbye");
			return;
		}
		else {
			var computerNumber = Math.floor(Math.random() * 11);
			console.log("CPU #: " +computerNumber);
			console.log("User #: " +num);
			test(num, computerNumber);
		}
	}
	else {
		alert("No problem, Goodbye");
		return;
	}
}

function test (myNumber, cpuNumber) {
	var count = 1;
	while (count<3) {
		if (myNumber == cpuNumber) {
		alert("Congratulations, you won!");
		return;
		}
		else {
			if(myNumber>cpuNumber) {
				var newGuess = prompt("Your number is bigger than mine, guess again: ");
				myNumber = newGuess;
				count++;
				}
			if(myNumber<cpuNumber) {
				var newGuess = prompt("Your number is smaller than mine, guess again: ");
				myNumber = newGuess;
				count++;
			}
		}
	}
	if (count==3) {
		alert("Sorry, you took too many guesses. The correct number was " +cpuNumber +". Better luck next time.");
	}
}