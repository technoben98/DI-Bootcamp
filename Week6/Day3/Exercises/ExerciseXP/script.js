// 🌟 Exercise 1 : Scope

// // #1
// function funcOne() {
//   let a = 5; // init variable outside condition
//   if (a > 1) {
//     // condition "a" bigger than 1
//     a = 3; // than "a" equals "3"
//   }
//   alert(`inside the funcOne function ${a}`); //because of a inited outside condition we get "a = 3"
// }

// // #1.1 - run in the console:
// funcOne();
// // #1.2 What will happen if the variable is declared
// // with const instead of let ?
// // answer: we get extension because we cant redeclarate const variable

// //#2
// let a = 0; // init out of conditions
// function funcTwo() {
//   a = 5; // change variable to 5
// }

// function funcThree() {
//   alert(`inside the funcThree function ${a}`); //show us relevant "a"
// }

// // #2.1 - run in the console:
// funcThree(); // this func give us a = 0. because already we didn't change it
// funcTwo(); // this func change a to 5
// funcThree(); // this func give us a = 5 because of previos func
// // #2.2 What will happen if the variable is declared
// // with const instead of let ?
// // answer: we get extention after first call of fincThree()

// //#3
// function funcFour() {
//   window.a = "hello";  // declaring global variable "a" with value "hello"
// }

// function funcFive() {
//   alert(`inside the funcFive function ${a}`); // call alert with "a"
// }

// // #3.1 - run in the console:
// funcFour(); //this method set our global variable "a"
// funcFive(); //and this method call alert with our variable

// //#4
// let a = 1; // declaring variable "a" with value "1" outside of method
// function funcSix() {
//   let a = "test"; // declaring variable "a" inside the method with value "test"
//   alert(`inside the funcSix function ${a}`); // call alert with a = "test" because this line use variable inside method
// }

// // #4.1 - run in the console:
// funcSix(); //give us text with a = "test"
// // #4.2 What will happen if the variable is declared
// // with const instead of let ?
// // answer: it will work because we use variable "a" that declarated inside of method in line 53 and no matter what happend with variable "a" outside method.

// //#5
// let a = 2; // variable a outside condition with value "2"
// if (true) {
//   // condition
//   let a = 5; //declaring new variable inside condition with value "5"
//   alert(`in the if block ${a}`); // call alert inside condition and because of this we get message with (a = 5)
// }
// alert(`outside of the if block ${a}`); // call allert outside condition and because of this we get message with variable "a = 2" that declared before condition

// // #5.1 - run the code in the console
// // #5.2 What will happen if the variable is declared
// // with const instead of let ?
// //answer: in this condition it doesn't matter bacause we dont change our variables

// 🌟 Exercise 2 : Ternary Operator

// const winBattle = () => true;

// const experiencePoints = winBattle() ? 10 : 1;
// console.log(experiencePoints);

// 🌟 Exercise 3 : Is It A String ?

// const isString = (value) => typeof value == "string";
// console.log(isString("history"));
// console.log(isString(1));

// 🌟 Exercise 4 : Find The Sum

// const sum = (a, b) => a + b;
// console.log(sum(5, 9));
// console.log(sum(3, 9));
// console.log(sum(5, 8));

// 🌟 Exercise 5 : Kg And Grams

// function convertToGrams(weightInKg) {
//   return weightInKg * 1000;
// }

// console.log(convertToGrams(5));

// const convertToGrams = function (weightInKg) {
//   return weightInKg * 1000;
// };

// console.log(convertToGrams(2.5));

// // difference is that declaration func you can use anywhere in code and expression must be defined before we can call it.

// const convertToGrams = (weightInKg) => weightInKg * 1000;

// console.log(convertToGrams(3));

// 🌟 Exercise 6 : Fortune Teller

// (function (numberOfChildren, partnerName, location, jobTitle) {
//   const sentence = `You will be a ${jobTitle} in ${location}, and married to ${partnerName} with ${numberOfChildren} kids.`;
//   const paragraph = document.createElement("p");
//   const body = document.body;
//   paragraph.textContent = sentence;
//   body.appendChild(paragraph);
// })(1, "Jack", "Los Angeles", "Software Engineer");

// 🌟 Exercise 7 : Welcome

// (function (userName) {
//   const userDiv = document.createElement("div");
//   userDiv.style.fontSize = "25px";

//   const nameSpan = document.createElement("span");
//   nameSpan.textContent = userName;
//   userDiv.appendChild(nameSpan);

//   const profilePic = document.createElement("img");
//   profilePic.src = "https://cdn-icons-png.flaticon.com/512/3106/3106773.png";
//   profilePic.style.width = "100px";
//   userDiv.appendChild(profilePic);

//   const navbar = document.getElementById("navBar");
//   navbar.appendChild(userDiv);
// })("John");

// 🌟 Exercise 8 : Juice Bar

function makeJuice(size) {
  let ingredients = [];

  function addIngredients(ingredient1, ingredient2, ingredient3) {
    ingredients.push(ingredient1, ingredient2, ingredient3);
  }

  function displayJuice() {
    sentence = `The client wants a ${size} juice, containing ${ingredients.join(
      ", "
    )}.`;
    const body = document.body;
    const paragraph = document.createElement("p");
    paragraph.textContent = sentence;
    body.appendChild(paragraph);
  }

  addIngredients("banana", "strawberry", "vanila");
  addIngredients("lyche", "mango", "blueberry");
  displayJuice();
}

makeJuice("large");
