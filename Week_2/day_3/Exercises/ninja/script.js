// 1

/*

var family = {

	brother : "Brad",

	sister : "Liza",

	mom : "Ilene",

	dad : "Bob"

};


for (key in family) {
	var value = family[key];
	console.log(value);
}

for (key in family) {
	console.log(key);
}

*/


// 2


/*
var building = {
    number_levels : 4,
    number_of_apt_by_level : {
        "1": 3,
        "2": 4,
        "3": 9,
        "4": 2,
    },
    name_of_tenants : ["Sarah", "Dan", "David"],
    number_of_rooms_and_rent: {
        "Sarah": [3, 2000],
        "Dan":  [4, 1000],
        "David": [1, 10]
    }
}

// Display the number of levels in the building:

console.log(building.number_levels);

// Display how many apartments are on level 1 and 3. Do the sum of these apartments

var SumApartments = building.number_of_apt_by_level['1'] + building.number_of_apt_by_level['3'];

console.log(SumApartments);

// Display the name of the second tenant and the number of rooms he has in his apartment

console.log("Tenant name: " +building.name_of_tenants[1] +". Number of rooms: " +building.number_of_rooms_and_rent["Dan"][0]);

// Check if the rent of Sarah plus the rent David is bigger than the rent of Dan.
// If it is than inform the owner that he has to inscrease the rent of Dan. 
// And change the rent of Dan accordingly inside the object.

var rentSandD = building.number_of_rooms_and_rent["Sarah"][1] + building.number_of_rooms_and_rent["David"][1];
console.log(rentSandD);

if (rentSandD>building.number_of_rooms_and_rent["Dan"][1]) {
	alert("Owner must increase Dan's rent");
	building.number_of_rooms_and_rent["Dan"][1] = '2000';
	console.log("Dan's new rent: " +building.number_of_rooms_and_rent["Dan"][1]);
}

*/


// 3

// var myGroceries = ["banana", "orange", "apple"];
// var total;

// var stock = { 
//     "banana": 6, 
//     "apple": 0, 
//     "orange": 32 
// }  

// var prices = {    
//      "banana": 4, 
//     "apple": 2, 
//     "orange": 1.5 
// } 

// // myBill();
// // console.log(total);
// console.log(stock.myGroceries[0]);

// // function myBill() {
// // 	 for (var i=0; i<myGroceries.length; i++) {
// // 	 	if (stock[(myGroceries[i])]>0) {
// // 	 		total = total + Number(prices[i]);
// // 	 		stock[(myGroceries[i])]--;
// // 	 	}
// // 	 }
// // 	 return total;
// // }


/* 1)

const family = {
	mom: "Ilene",
	dad: "Bob",
	brother: "Brad",
	sister: "Liza"
}

Object.keys(family).forEach(key => {
	console.log(key)
});

Object.values(family).forEach(value => {
	console.log(value)
});
*/



/* 2)

var building = {
    number_levels : 4,
    number_of_apt_by_level : {
        "1": 3,
        "2": 4,
        "3": 9,
        "4": 2,
    },
    name_of_tenants : ["Sarah", "Dan", "David"],
    number_of_rooms_and_rent: {
        "Sarah": [3, 2000],
        "Dan":  [4, 1000],
        "David": [1, 10]
    }
}
*/

// Display the number of levels in the building:
// 		console.log(building.number_levels);

//Display how many apartments are on level 1 and 3. Do the sum of these apartments
/*
		var lev1 = prompt("Enter a level: ");
		var lev2 = prompt("Enter another level: ");
		var both = aptsPerLevel(lev1)+aptsPerLevel(lev2);

		alert("On levels " +lev1 +" and " +lev2 +" there are " +both +" total apartments.");

		function aptsPerLevel (level) {
			var apts = building.number_of_apt_by_level[level];
			return apts;
		}
*/

//Display the name of the second tenant and the number of rooms he has in his apartment
/*
		var tenNumber = prompt("Enter a tenant number: ");

		var tenName = building.name_of_tenants[tenNumber-1];
		alert("Tenant's name is: " +tenName);

		var rooms;
		function findRooms (name) {
			Object.entries(building.number_of_rooms_and_rent).forEach(item => {
				if (item[0] == name) {
					rooms = (item[1][0]);
				}
			})
			return rooms;
		}

		totalRooms = findRooms(tenName);
		console.log("totalRooms: " + totalRooms);

		alert(tenName +"'s apartment has "+ totalRooms  +" rooms.");
*/

// Check if the rent of Sarah plus the rent David is bigger than the rent of Dan.
// If it is than inform the owner that he has to inscrease the rent of Dan. 
// And change the rent of Dan accordingly inside the object.

/*
		var rentSandD = building.number_of_rooms_and_rent["Sarah"][1] + building.number_of_rooms_and_rent["David"][1];
		console.log(rentSandD);

		if (rentSandD>building.number_of_rooms_and_rent["Dan"][1]) {
			alert("Owner must increase Dan's rent");
			building.number_of_rooms_and_rent["Dan"][1] = '2000';
			console.log("Dan's new rent: " +building.number_of_rooms_and_rent["Dan"][1]);
		}

*/




/* 3)

var myGroceries = ["banana", "orange", "apple"];

var stock = { 
    "banana": 6, 
    "apple": 0, 
    "orange": 32 
}  

var prices = {    
     "banana": 4, 
    "apple": 2, 
    "orange": 1.5 
} 


		var currentItem;
		var tab = 0;
		function myBill() {
			for (i=0; i<myGroceries.length; i++) {
				currentItem = myGroceries[i];
				if (stock[currentItem]>0) {
					tab = tab + (prices[currentItem]);
					stock[currentItem] --;
					console.log("New stock " +currentItem +": "+stock[currentItem])
				}
			}
			console.log(tab);
		}

		myBill();

*/



/* 4)

*/

		var people = {

			person1: {
				fullName: "Jim Brown",
				mass: 140,
				height: 1.95,
				bmi: calcBMI(290,1.95),
			},

			person2: {
				fullName: "Michael Scott",
				mass: 95,
				height: 1.75,
				bmi: calcBMI(175,1.75),
			}
		}

		function calcBMI (m,h) {
			var answer = m/(h*h);
			return answer;
		}

		console.log(people.person1["bmi"]);
		console.log(people.person2["bmi"]);