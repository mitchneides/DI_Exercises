function check_radio_question(radio_name){
	var radios = document.getElementsByName(radio_name);
	for (radio of radios) {
		if (radio.checked) {
			return radio.value;
		}
	}
}

var answerArray = [];
function makeAnswerArray() {
	for(var i=1; i<6; i++) {
		var currentQuestion = 'q'+i;
		var answer = check_radio_question(currentQuestion);
		answerArray.push(answer);
		currentQuestion = '';
	}
	console.log(answerArray);
	//this array will be compared against the party arrays
	var userScore = 0;
 	for(var j=1; j<6; j++) {
 		var currentQuestion_score = 'q'+j;
 		var answer_score = check_radio_question(currentQuestion_score);
 		userScore = userScore + Number(answer_score);
 		currentQuestion_score = '';
 	}
 	console.log('score: '+userScore/5);
 	//displays where user falls on a scale of -2 to 2 (liberal to conservative)

 	answerArray = [];
 	//if button is pressed multiple times, array won't contain multiples of the data
}
