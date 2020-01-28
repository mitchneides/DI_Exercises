var noun = document.getElementById('noun');
var adj = document.getElementById('adjective');
var person = document.getElementById('person');
var button = document.getElementById('lib-button');

button.addEventListener('click', function libIt(e){
	var storyDiv = document.getElementById("story");
            storyDiv.innerHTML = 
            "I gave " +person.value
            + " $100, just to see what he would do with it."
            + " He immediately went and bought a " +noun.value
            +". I thought it was " +adj.value +", but he thinks it is the coolest thing ever.";
});

