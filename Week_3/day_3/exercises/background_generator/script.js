var css = document.querySelector("h3");
var bottom = document.querySelectorAll("h3")[1];
var color1 = document.querySelector('.color1');
var color2 = document.querySelector('.color2');
var body = document.getElementById("gradient");

color1.addEventListener("input" , setGradient);
color2.addEventListener("input" , setGradient);

function setGradient() {
	body.style.background = 
	"linear-gradient(to right, " 
	+ color1.value 
	+ ", " 
	+ color2.value 
	+ ")";

	css.textContent = body.style.background + ";";
}

var button = document.createElement('button');
button.innerText = "Generate random colors";
button.style.color = 'white';
button.style.backgroundColor = "rgba(0,0,0,.5)";
button.style.borderColor = "rgba(0,0,0,.5)";
bottom.append(button);

button.addEventListener('click', function(e){
	body.style.background = 
	"linear-gradient(to right, " 
	+ generateRandomColor() 
	+ ", " 
	+ generateRandomColor() 
	+ ")";

	css.textContent = body.style.background + ";";
});

function generateRandomColor()
{
    var randomColor = '#'+Math.floor(Math.random()*16777215).toString(16);
    console.log(randomColor);
    return randomColor;
}