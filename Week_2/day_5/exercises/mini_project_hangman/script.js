const wordOptions = ["variation", "universe", "speeding", "stupidity", "annimation", "assignment"];
var attempts = 0;
var areSame = false;

playTheGame();
function playTheGame () {
	var c = confirm("Would you like to play the game?");
	if (c == true){
		chooseWord(wordOptions);
		replaceLetters(theWord);
		makeAnswerArray(theWord);
		while (attempts<10 && areSame==false) {
			takeGuess();
			checkGuess(guessLetter);
			compare();
		}
		if (attempts>=10 && areSame==false) {
			alert("Too many attempts. You lose. The correct answer was: " +theWord);
		}
		if (attempts<=10 && areSame==true) {
			alert("You won! You guessed " +theWord +" in " +attempts +" attempts.");
		}
	}
	else {
		alert("No problem, Goodbye");
		return;
	}
}


// chooseWord(wordOptions);
var theWord;
function chooseWord (array) {
	var numOptions = Number(array.length);
	var wordNumber = Math.floor(Math.random() * numOptions);
	theWord = array[wordNumber];
	console.log("Word is: " +theWord);
	return theWord;
}
//function randomly assigns word for game

// replaceLetters(theWord);
var starWord;
function replaceLetters (word) {
	var len = word.length;
	starWord = [];
	for (i=0; i<len; i++) {
		starWord.unshift("*");
	}
	starWord[0] = word.charAt(0);
	starWord[len-1] = word.charAt(len-1);
	console.log(starWord);
	return starWord;
}
//function makes all letters *'s (except first and last)


// makeAnswerArray(theWord);
var answerWord;
function makeAnswerArray (word) {
	var len = word.length;
	answerWord = [];
	for (i=0; i<len; i++) {
		answerWord.push(word.charAt(i));
	}
	console.log("Answer array: " +answerWord);
	return answerWord;
}
//function makes array of the answerWord

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
//function checks if a letter was input

// takeGuess();
var guessLetter;
function takeGuess () {
	guessLetter = prompt(starWord.join("") + "     -      Guess a letter: ");
	while (isChar(guessLetter) == false || guessLetter.length>1) {
		alert("Invalid guess. You must guess a letter, and only 1 letter.")
		guessLetter = prompt(starWord.join("") + "     -      Guess a letter: ");
	}
	attempts++;
	console.log("Attempts: " +attempts);
	return guessLetter;
}
//function takes a guess and confirms that it is valid



// checkGuess(guessLetter);
function checkGuess (guess) {
	var something = false;
	for (var i=1; i<answerWord.length; i++) {
		if (answerWord[i]==guess) {
			starWord[i] = guess;
			console.log("starWord: "+starWord);
			something = true;
		}
	}
	if (something==true) {
		alert("Nice! You got " +guess +"!");
		return;
	}
	else {
		alert("Incorrect. Try harder.");
		return;
	}
}
// function checks the guess and updates starWord


// compare();
function compare () {
	var z = 0;
	for (i=0; i<starWord.length; i++) {
		if (starWord[i] == "*") {
			z++;
		}
	}
	if (z==0) {
		areSame = true;
	}
	return;
}
//function takes the current star word and compares it to the answer word
//if they are the same, areSame changes to true
