//  ///////////////Notes//////////////////
/*
function setTime(){
	setTimeout(function(){
		console.log("Hello");
	},3000);
}
//When called, function logs hello to console after 3 sec

var id;
function setInter(){
	id = setInterval(function(){
		console.log("Hello");
	},3000);
}
//When called, every 3 seconds logs hello to console
//Doesnt stop until interval is cleared (below)

function clearInter(){
	clearInterval(id);
}
//When called, stops interval loop
*/


//    ////////////box run diag exercise///////////////
/*
var body = document.getElementsByTagName('body')[0];

var outer_div = document.createElement('div');
outer_div.setAttribute('id', 'container');
body.appendChild(outer_div);

var inner_div = document.createElement('div');
inner_div.setAttribute('id', 'animate');
outer_div.appendChild(inner_div);

var button = document.createElement('button');
button.innerText = "Click me";
body.append(button);

button.addEventListener('click', myMove);

function myMove() {
	var pos = 0;
	let id = setInterval(function() {
		if (pos == 350) {
			clearInterval(id);
		}
		else {
			pos++;
			inner_div.style.top = pos + "px";
			inner_div.style.left = pos + "px";
		}
	},5)
}
*/


//        //////tic tac toe///////////////////

var board_array = ['-1','-1','-1','-1','-1','-1','-1','-1','-1'];
var track_turns = [];
var who_is_up = document.getElementById('who_is_up');
// who_is_up.innerText = turnSign +"'s turn";
body.append(who_is_up);

var turn = 1;
var turnSign = "X";


function assignTurn() {
	if(turn%2 == 0) {
	turnSign = 'O';
	}
	else {
		turnSign = 'X';
	}
};






play();
function play(x,buttonNum) {
	var buttonClicked = document.getElementsByClassName('button')[buttonNum];
	console.log('buttonNum: '+buttonNum);
	console.log('turn: '+turn)

	assignTurn();
	console.log('turnSign: ' +turnSign);

	board_array[buttonNum] = turnSign;
	console.log(board_array);

	buttonClicked.innerText = turnSign;

	turn++;
	console.log('nextturn: '+turn);
}



// ////////////////
