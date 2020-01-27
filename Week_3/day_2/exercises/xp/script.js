//Exercise 1

//1
var paras = document.querySelectorAll("article p");
for (para of paras) {
	para.className = "para_article";
}

//2
var last_para = document.body.firstElementChild.lastElementChild;
document.body.firstElementChild.removeChild(last_para);

//skip 3 - Ziv
//4
var h1s = document.getElementsByTagName("h1");
for(h1 of h1s) {
	h1.style.fontSize = getRand() + "px";
}
function getRand() {
	rand = Math.floor(Math.random() * 100) + 1;
	return rand;
}

//5
var first_para = document.querySelector('p');
first_para.addEventListener("click", hidePara);
function hidePara(){
	document.body.firstElementChild.removeChild(first_para);
}

//6
var second_para = document.querySelectorAll('p')[1];
second_para.addEventListener("click", fadePara);
function fadePara(){
	setTimeout(function() {
    $(second_para).fadeOut();
	}, 2000);
}

//7
//????????????????????



//Exercise 2

//1
getBoldItems()
function getBoldItems() {
	var bolds = document.getElementsByTagName("strong");
	console.log(bolds);
	return bolds;
}

//2
function highlight() {
	for(bold of getBoldItems()) {
		bold.style.color = "blue";
	}
}

function returnNormal() {
	for(bold of getBoldItems()) {
		bold.style.color = "black";
	}
}

//3
var bold_para = document.body.firstElementChild.nextElementSibling;
bold_para.addEventListener("mouseover", highlight);
bold_para.addEventListener("mouseout", returnNormal);