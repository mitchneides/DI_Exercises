
// const rootDiv = document.getElementById("root");
// //assign 'rootDiv' to root location
// let but = document.createElement('button');
// //create button
// but.innerText = 'Click';
// //write button text
// but.setAttribute('class', 'a');
// // sets a class (a) to the button

// let inp = document.createElement('input');
// inp.setAttribute('type','text');
// inp.setAttribute('placeholder','enter your email');
// inp.setAttribute('id','emailInput');
// //creates an input box, gives it a placeholder and an id

// but.addEventListener('click', function(event){
// 	let myinput = document.getElementById('emailInput');
// 	validate(myinput.value);
// 	console.log(myinput.value);
// });
// //on click, takes the input from the textbox and logs it to the console

// /*
// inp.addEventListener('keypress', function(e){
// 	console.log(e.target.value);
// });
// //on every letter that is typed, will console log what is in the box
// */

// inp.addEventListener('keypress', function(e){
// 	if (e.keyCode === 13) {
// 		console.log(e.target.value);
// 		validate(e.target.value);
// 		e.target.value = "";
// 	}
// });
// //on every keypress, checks if key pressed was 'enter'
// //if it was, checks if the value entered was text (vs blank spaces)
// //logs entire typed value in the console and
// //returns input box (e.target.value) back to blank

// const validate = (val) => {
// 	if(val.trim().length == 0) {
// 		alert("Enter a valid email");
// 	}
// 	else {
// 		alert("Your email is: " +val);
// 	}
// }


// /*
// but.addEventListener('click', function(event){
// 	console.log(event.clientX);
// 	event.target.innerText = 'click meeee';
// 	//changes button text
// 	event.target.classList.add('d');
// 	console.log(event.target);
// });
// //on click, button will do the function
// */


// rootDiv.appendChild(inp);

// rootDiv.appendChild(but);
// //append button to root (/webpage body)




const root = document.getElementById("root");

root.classList.add('box');

root.setAttribute('draggable', 'true');

root.addEventListener("dragend" , function(e) {
	let x = e.clientX;
	let y = e.clientY;
	(console.log(x,y));
	//marks positions where the mouse is on screen
	root.style.left = x+"px";
	root.style.top = y+"px";
	//sets the 'left' and 'top' values (from CSS page) to 
	//mouse coordinates
} );



root.addEventListener('mouseover', function(e) {
	changeColor("red", e.target);
});
// function receives e - event
//pass e.target (which = root) through changeColor function
//changeColor function takes elem (which here = e.target = root)
// and color

root.addEventListener('mouseout', function(e) {
	changeColor("white", e.target);
});

root.addEventListener('mousedown' , function(e) {
	changeColor("blue", e.target);
});

root.addEventListener('mouseup' , function(e) {
	changeColor("orange", e.target);
});


function changeColor(color, elem) {
	elem.style.backgroundColor = color;
}

//1 function instead of 4:
/*
function changeRed(elem) {
	elem.style.backgroundColor = 'red';
}

function changeWhite(elem) {
	elem.style.backgroundColor = 'white';
}

function changeBlue(elem) {
	elem.style.backgroundColor = 'blue';
}

function changeOrange(elem) {
	elem.style.backgroundColor = 'orange';
}
*/

