function botsOut() {
	let root = document.getElementById("root");
	//specifies location of root
	root.className = 'box-grid box-center';
	//adds classes box-grid and box-center to whole div "root"

	for (robot of robots) {
		var infoDiv = document.createElement('div');
		//creates div for each robot

		infoDiv.classList.add("dot_border");
		//assigns a class (which gives dotted border)

		let graphic = document.createElement('img');
		let robotName = document.createElement('h2');
		let userName = document.createElement('p');
		let email = document.createElement('p');
		//creates each section within the div
		
		graphic.setAttribute("src","https://robohash.org/" + robot["id"] +"?size=200x200");
		robotName.innerText = robot["name"];
		userName.innerText = robot["username"];
		email.innerText = robot["email"];
		//fills each section 

		infoDiv.appendChild(graphic);
		infoDiv.appendChild(robotName);
		infoDiv.appendChild(userName);
		infoDiv.appendChild(email);
		//adds each section to div

		root.appendChild(infoDiv);
		//adds div to page(root) from HTML
	}
}

function changeBorder() {
	var infoDiv = document.getElementsByClassName('dot_border');
	//finds the holder boxes according to the class that 
	// was assigned above (to make the original border)
	for (div of infoDiv) {
		div.classList.toggle("solid_border");
	}
}