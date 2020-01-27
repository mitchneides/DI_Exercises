function addItem() {
	var item = prompt("Enter a grocery item to add to your list: ");
	var li = document.createElement('li');
	li.innerText = item;
	document.getElementById('shoppingList').appendChild(li);
}

function clearAll() {
	document.getElementById('shoppingList').innerText = '';
}

document.firstElementChild.style.backgroundColor = "#496D89";