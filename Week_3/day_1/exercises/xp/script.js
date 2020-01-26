/*
For each of the questions, find 2 WAYS of accessing :
1. The div DOM node?
2. The ul DOM node?
3. The second li (with Pete)?
*/

/*
//1.1
let elem = document.body.firstElementChild;
console.log(elem);
//1.2
console.log(document.body.childNodes[1]);

//2.1
console.log(document.body.firstElementChild.nextElementSibling);
//2.2
console.log(document.body.childNodes[3]);

//3.1
console.log(document.body.childNodes[3].childNodes[3]);
//3.2
console.log(document.body.lastElementChild.previousElementSibling.lastElementChild);
*/




/*
1. Change the background color of the div DOM node to lightblue and 
inscrease its padding
2. Don’t display the first name (John) and give a border to the second name (Pete)
3. Change the font size of the whole HTML
4. Bonus:
Check if the background color of the div is lightblue, 
if yes alert “Hello x and y” (x and y are the new users)
*/

/*
//1
let workingDiv = document.body.firstElementChild;
workingDiv.style.backgroundColor = "lightblue";
workingDiv.style.padding = "20px";
console.log(workingDiv);

//2
let list = document.body.childNodes[3];
console.log(list);
list.removeChild(list.childNodes[1]);
list.style.border = "1px solid black";

//3
let whole = document.body;
console.log(whole);
whole.style.fontSize = "22px";
// ???????????????????

//4
if (workingDiv.style.backgroundColor == "lightblue") {
	alert("Hello x and y");
}
*/


/*
For the questions below, use at least 2 PROPERITIES to access :
1. The <div> node
2. The <ul> nodes,. and render all of it’s children one by one
3. The first <li> of each <ul>
*/

// var thisDiv = document.getElementsByClassName("list")[0].previousElementSibling;
// //1.2
// console.log(thisDiv);
// //1.2
// console.log(document.getElementById('container'));

// //2.1
// var unorderedLists = document.getElementsByClassName("list");
// console.log(unorderedLists);
// //2.

// // var list1 = unorderedLists[0];
// // var list2 = unorderedLists[1];

// // console.log(list1.innerText);
// // console.log(list2.innerText);

// for (unorderedList of unorderedLists) {
// 	console.log(unorderedList.innerText);
// }
// //??????????????????????????????

// //3.1
// console.log(unorderedLists[0].firstElementChild.innerText);
// console.log(unorderedLists[1].firstElementChild.innerText);

// //3.2
// console.log(unorderedLists[0].lastElementChild.previousElementSibling.innerText);
// console.log(unorderedLists[1].lastElementChild.previousElementSibling.innerText);


/*
Change the name “Pete” by “Richard”
Change each first name of the <ul> by your name
Add add the end of each <ul>, a paragraph that says “Hey students”
Delete the <li> Sarah
Bonus:
Change the class of <ul> by “student_list”
Add a class “university” to the first <ul>
*/

//1
// var richard = document.createTextNode("Richard");

// var pete = document.body.childNodes[3].lastElementChild;
// console.log(pete);

// document.body.childNodes[3].replaceChild(richard, pete);



//2
var unorderedLists = document.getElementsByClassName('list');
console.log(unorderedLists);

var mitch = document.createTextNode("Mitch");

var john = document.body.childNodes[3].firstElementChild;
console.log(john);

document.body.childNodes[3].replaceChild(mitch, john);

var david = document.body.childNodes[5].firstElementChild;

var mitch = document.createTextNode("Mitch");

document.body.childNodes[5].replaceChild(mitch,david);


var para = document.createElement('p');
para.innerText = "Hey students";
document.body.childNodes[3].appendChild(para);

var para = document.createElement('p');
para.innerText = "Hey students";
document.body.childNodes[5].appendChild(para);


var sarah = document.body.childNodes[5].childNodes[3];
console.log(sarah);
document.body.childNodes[5].removeChild(sarah);
