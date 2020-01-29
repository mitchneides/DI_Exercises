const root = document.getElementById('root');
root.style.display = 'flex';
root.style.justifyContent = 'space-between';

let abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split('');

for (letter of abc) {
	var currentBox = makeBox(letter);
	// currentBox.setAttribute('id', abc.indexOf(letter));
	root.append(currentBox);
	currentBox.addEventListener("dragend" , function(e) {
		console.log(e.target.innerText);
		let x = e.clientX;
		let y = e.clientY;
		e.target.style.left = x+"px";
		e.target.style.top = y+"px";
		e.target.style.position = "fixed";
		console.log(x,y);
	} );
}

function makeBox(letter) {
	newDiv = document.createElement('div');
	newDiv.style.border = '1px solid black';
	newDiv.style.width = '20px';
	newDiv.style.height = '20px';
	newDiv.style.display = 'flex';
	newDiv.style.justifyContent = 'center';
	newDiv.innerText = letter;
	newDiv.setAttribute('draggable', 'true');
	return newDiv;	
}