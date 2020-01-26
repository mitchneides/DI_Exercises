let allBooks = [
	{
		title: "Harry Potter",
		author: "J.K. Rowling",
		image: 'hp.jpeg',
		alreadyRead: true,
	},
	{
		title: "The Confessor",
		author: "Daniel Silva",
		image: "confessor.jpeg",
		alreadyRead: true,
	},
];

for (var i=0; i<allBooks.length; i++) {
	var bookP = document.createElement('p');
	var bookDescription = document.createTextNode(allBooks[i].title + ' by ' + allBooks[i].author);
	// if(allBooks[i].alreadyRead == true) {
	// 	bookDescription.style.color = "red";
	// }
	var bookImage = document.createElement('img');
	bookImage.src = allBooks[i].image;
	bookImage.width = "100";
	bookP.appendChild(bookImage);
	bookP.appendChild(bookDescription);
	document.body.appendChild(bookImage);
	document.body.appendChild(bookP);
}
