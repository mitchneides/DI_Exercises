//Write a JavaScript for loop that will iterate from 0 to 15. For each iteration,
//it will check if the current number is odd or even,
//and display a message to the screen.
//Sample Output:
//"0 is even"
//"1 is odd"
//"2 is even"

/* MY ANSWER:

for (var i=0; i<=15; i++) {
  if (i%2 == 0) {
    alert(i +" is even.");
   }
  else {
    alert(i +" is odd.")
  }
}

*/





/*
​//Write a JavaScript program which iterates the integers from 1 to 100. 
//But for multiples of three print "Fizz" instead of the number and
//for the multiples of five print "Buzz".
//For numbers which are multiples of both three and five print "FizzBuzz".
​*/

/* MY ANSWER:

var count;

for (var i=1; i<=100; i++) {
    if ((i%3 == 0) && (i%5 != 0)) {
      count = "Fizz";
    }
    else if ((i%5 == 0) && (i%3 != 0)) {
      count = "Buzz";
    }
    else if ((i%3 == 0) && (i%5 == 0)) {
      count = "FizzBuzz";
    }
    else {
      count = i;
    }
    console.log(count);
}

*/








//Write a JavaScript program which compute, the average marks of the following students
//Then, this average is used to determine the corresponding grade.

// var students = [
//   ['David', 80],
//   ['Vinoth', 77],
//   ['Divya', 88],
//   ['Ishitha', 95],
//   ['Thomas', 68]
// ];
//  Range	Grade
//  F <60
//  D <70
//  C <80
//  B <90
//  A <100



/* MY ANSWER:

var rawTotal = 0;
var grade="";

for (var i=0; i<students.length; i++) {
  rawTotal = rawTotal + Number(students[i][1]);
}
console.log("Raw Total: " +rawTotal);

var avg = rawTotal/students.length;
console.log("Average: " +avg);

if (avg<60) {
  grade = "F"
}
else if (avg<70) {
  grade = "D"
}
else if (avg<80) {
  grade = "C"
}
else if (avg<90) {
  grade = "B"
}
else if (avg<=100) {
  grade = "A"
}

console.log("The average grade is: " +grade);








​
​
*/




// Write a JavaScript program to construct the following pattern,
// using a nested for loop.
//  *
//  * *
//  * * *
//  * * * *
//  * * * * *



/* MY ANSWER:

var star = "* ";

for (var i = 1; i<6; i++) {
  console.log(star.repeat(i));
}


---OR---

var temp = "";

for (var i =0; i<5; i++) {
  temp = temp + "* "
  console.log(temp);

}


*/








/*


//Complete the below questions using this array:

//Create an array using forEach that has all the usernames with a "!" to each of the usernames
​
//Create an array using for loop that has all the usernames with a "?" to each of the usernames
​
//Filter the array to only include users who are on team: red
​
//Find out the total score of all users


*/

 
const array = [
  {
    username: "john!?",
    team: "red",
    score: 5,
    items: ["ball", "book", "pen"]
  },
  {
    username: "becky!",
    team: "blue",
    score: 10,
    items: ["tape", "backpack", "pen"]
  },
  {
    username: "susy!",
    team: "red",
    score: 55,
    items: ["ball", "eraser", "pen"]
  },
  {
    username: "tyson",
    team: "green",
    score: 1,
    items: ["book", "pen"]
  },
];
/*


​*/
var newArr = [];

array.forEach(element => newArr.push(element));
console.log(newArr);










/*
​
BONUS: create a new list with all user information, but add "!" to the end of each items they own.
​
BONUS: Write a JavaScript program to construct the following pattern,
using a nested for loop.
         *
       * * *
     * * * * *
   * * * * * * *
 * * * * * * * * *



 */