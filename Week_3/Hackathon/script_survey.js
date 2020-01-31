add_event_listeners();
function add_event_listeners() {
// initializes page, setting event listeners to each button
// and activates highlight for selected buttons
	var answer_buttons = document.getElementsByClassName('btn');
	for (button of answer_buttons) {
		button.addEventListener("click", function() {
  			let buttons_in_group = this.parentNode.children;
  			for (current_button of buttons_in_group) {
  				current_button.classList.remove("active");
  			}
  			this.classList.add('active');
  			console.log(this.getAttribute('name')+ ": " +this.value);
		});
	}
}


function make_user_answer_array() {
// called on submit survey button
// creates array of all user's answers
	var user_answer_array = [];
	for(var i=1; i<26; i++) {
		var currentQuestion = 'q'+i;
		var answer = check_responses(currentQuestion);
		user_answer_array.push(answer);
		currentQuestion = '';
	}
	console.log(user_answer_array);

	compare_all(user_answer_array);

}

function check_responses(question_name) {
// returns (to make user answer array) which button was 
// selected for each question
	var answer_buttons_of_question = document.getElementById(question_name).lastElementChild.children;
	for (var j = 0; j < answer_buttons_of_question.length; j++) {
		if (answer_buttons_of_question[j].getAttribute('class') == 'btn active') {
			let the_value = answer_buttons_of_question[j].getAttribute('value');
			return the_value;
		}
	}
}

// ///////////////////////////////////////////

const parties = {
	"likud": [-1,-1,2,-1,-2,0,2,1,-1,-2,1,-2,-1,1,-2,0,1,2,-1,1,-1,0,-2,-1,0],
	// "kl": [1,1,1,1,1,0,0,0,0,0],
	"joint_list": [2,2,-1,-2,-2,1,-2,0,1,-2,1,2,1,-1,-1,1,0,-2,2,2,-2,-2,2,2,2],
	// "yamina": [2,2,2,2,2,2,2,2,2,2]
	"test": [-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2]
}
// object holds answer array for each party


let comparisons = {}
// object to be filled with arrays for comparison of each political party
// to be filled with x's(match) and o's(non-match)
let scores = {}
// CHECK IF USED
let every_party_final_score = [];
// array holding the score for matches with each party

function compare_all(user_answers){	
// loops through parties object and compares it with the user's answers
	let keys = Object.keys(parties)
	for(key of keys){
		comparisons[key] = make_comparison(user_answers, parties[key]);
	}
}



// ////////////////////////////////////////


// function make_comparison(user_answers, pre_set){
// // fills comparison array with x's and o's
// 	let comparison_array = []
// 	for (let i = 0; i <= user_answers.length -1; i++){
// 		value = (user_answers[i] == pre_set[i] ? "X" : "O")
// 		comparison_array[i] = value;
// 	}
// 	score_all(comparison_array);
// }


function make_comparison(user_answers, pre_set){
// fills comparison array with x's, y's and o's
	let comparison_array = []
	for (let i = 0; i <= user_answers.length-1; i++){
		if (user_answers[i] == pre_set[i]) {
			value = "X";
		}
		else if (user_answers[i]>0 && pre_set[i]>0) {
			value = "Y";
		}
		else if (user_answers[i]<0 && pre_set[i]<0) {
			value = "Y";
		}
		else {
			value = "O";
		}
	comparison_array[i] = value;
	}
	score_all(comparison_array);
}


function score_all(comparisons){
// loops through all comparisons, counts # of x's for each array and gives amnt
	var score = 0;
	let keys = Object.keys(comparisons)
	for(key of keys){
		if (comparisons[key] == 'X') {
			score++;
		}
		else if (comparisons[key] == 'Y') {
			score = score + 0.5;
		}
	}
	every_party_final_score.push(score);
	console.log('every_party_final_score: ' +every_party_final_score);
	get_score(every_party_final_score);
}


// function score_all(comparisons){
// // loops through all comparisons, counts # of x's for each array and gives amnt
// 	var score = 0;
// 	let keys = Object.keys(comparisons)
// 	for(key of keys){
// 		if (comparisons[key] == 'X') {
// 			score++;
// 		}
// 	}
// 	every_party_final_score.push(score);
// 	console.log('every_party_final_score: ' +every_party_final_score);
// 	get_score(every_party_final_score);
// }



// //////////////////////////////////////////////



function get_score(final_scores_array){
// looks in every_party_final_score and decides which party has the highest score
// every_party_final_score is arranged in same order as the list of parties
	var max = final_scores_array[0];
    var maxIndex = 0;
    for (var i = 1; i < final_scores_array.length; i++) {
        if (final_scores_array[i] > max) {
            maxIndex = i;
            max = final_scores_array[i];
        }
    }
    console.log('max is at index: '+maxIndex);
    get_winner_party_name(maxIndex);
}

function get_winner_party_name(index) {
	let keys = Object.keys(parties)
	winner = keys[index];
	console.log('Winning party is: '+winner);
	return winner;
}






//    ///// old  ///////
// function check_radio_question(radio_name){
// 	var radios = document.getElementsByName(radio_name);
// 	for (radio of radios) {
// 		if (radio.checked) {
// 			return radio.value;
// 		}
// 	}
// }

// var answerArray = [];
// function makeAnswerArray() {
// 	for(var i=1; i<6; i++) {
// 		var currentQuestion = 'q'+i;
// 		var answer = check_radio_question(currentQuestion);
// 		answerArray.push(answer);
// 		currentQuestion = '';
// 	}
// 	console.log(answerArray);
// 	//this array will be compared against the party arrays
// 	var userScore = 0;
//  	for(var j=1; j<6; j++) {
//  		var currentQuestion_score = 'q'+j;
//  		var answer_score = check_radio_question(currentQuestion_score);
//  		userScore = userScore + Number(answer_score);
//  		currentQuestion_score = '';
//  	}
//  	console.log('score: '+userScore/5);
//  	//displays where user falls on a scale of -2 to 2 (liberal to conservative)

//  	answerArray = [];
//  	//if button is pressed multiple times, array won't contain multiples of the data
// }