/*

const basket = ['apples', 'oranges', 'grapes'];

//1

for (let x=0; x<basket.length; x++) {
	console.log(basket[x]);
}

//2

for (i in basket) {
	console.log(basket[i]);
}

//3

for (elem of basket) {
	console.log(elem);
}

// 1-3 all give the same answer


//4 

basket.forEach( (elem, index) => {
	console.log(elem, index);
}

	);




const detailedBasket = {
	apples : 5,
	oranges : 10,
	pears : 20
}

for (x in detailedBasket) {
	console.log(detailedBasket);
	// console.log(x);
	// console.log(detailedBasket[x]);
}

*/

/*
const detailedBasket = {
	Apples: 5,
	Oranges: 10,
	Grapes: 1000
}


Object.keys(obj) 
//keys

Object.values(obj)
//values

Object.entries(obj)
//keys values

Ex:


Object.keys(detailedBasket).forEach( key => {
	console.log(key);
});
//apples then oranges then grapes

Object.values(detailedBasket).forEach( value => {
	console.log(value);
});
//5 then 10 then 1000

Object.entries(detailedBasket).forEach( ent => {
	console.log('entries', ent);
});
// ["Apples", 5] then ["Oranges", 10] then ["Grapes", 1000]

*/

var arr = [5, 0, 9, 1, 7, 4, 2, 6, 3, 8];
var holder;

for (i=0; i<arr.length; i++) {
	for (j=i; j<arr.length; j++)
		if (arr[i]<arr[j]) {
			temp = arr[i];
			arr[i] = arr[j];
			arr[j] = temp;
		}
}
console.log(arr);