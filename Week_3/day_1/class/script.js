/*
let elem = document.getElementById('content');
elem.setAttribute('width', '100');

let div1 = document.getElementById('page');
let att = div1.getAttribute('ziv');
console.log(att);
// displays 'eeeee'

div1.setAttribute('ziv', 'gggg');
att = div1.getAttribute('ziv');
console.log(att);
// displays 'gggg'
*/

/*
let elem = document.getElementById('title');
console.log(elem.innerText);
// displays 'page title'
*/

/*
let elem = document.getElementById('content');
//declares what section we will be working with

let myH1 = document.createElement('h1');
//creates a blank, new h1

myH1.innerText = "Whatever I want";
//writes text of h1, but is currently only stored in memory

elem.appendChild(myH1);
//adds h1 to bottom of content div
*/

/*
let elem = document.getElementById('content');
//declares what section we will be working with

let arr = ['ziv', 'jason', 'sara', 'rachel'];

for(var i=0; i<arr.length; i++) {
	let user = document.createElement('h4');
	//we will be creating h4's
	user.innerText = arr[i];
	//declares what the text of each h4 will be
	elem.appendChild(user);
	//adds each h4 to 'content' div
}
*/

/*
Exercise 1: Traversing the DOM
Knowing how to traverse the DOM using JavaScript provides a foundation
to altering an HTML page in real time.
Using the HTML markup in Listing 1, perform these tasks:
1. Use the firstElementChild / firstChild property to access an element.
2. Use the lastElementChild / lastChild  property to access an element.
3. Use the nextElementSibling / nextSibling  property to access an element.
4. Use the previousElementSibling / previousSibling  property to access an element.
5. Use the parentNode property to access an element.
6. Use the childNodes property to access a group of child elements.
*/

// let elem = document.getElementById('content');
// console.log(elem.parentNode);
// console.log(elem.childNodes);


/*
Exercise 2: Targeting nodes b
In exercise 1, you learned how to target nodes in several ways.
Continuing to use the markup in Listing 1, perform the following tasks:
1. Retrieve the value of a node using nodeValue / innerText / innerHTML.
2. Change the value of a node using nodeValue / innerText / innerHTML.
3. Retrieve the value of a node attribute.
4. Change the value of a node attribute.
*/




// let txt = document.createTextNode('abcd');
// elem.appendChild(txt);
// console.log(txt.nodeValue);

// console.log(elem.innerText);




/*
Exercise 3: Manipulating the DOM
Now that you know how to traverse the DOM and alter node values,
the next logical step is to learn how to add, remove, and replace nodes.
Perform the following tasks:
1. Use the appendChild method to add a node.
2. Use the insertBefore method to add a node.
3. Use the removeChild method to remove a node.
4. Use the replaceChild method to replace a node.
Collapse
*/


let header = document.getElementById('header');

let title = document.getElementById('title');

let elem1 = document.createElement('h1');
elem1.innerText = "Hello World";

header.insertBefore(elem1,title);
//inserts elem1 before title, within the header node

// header.removeChild(title);











