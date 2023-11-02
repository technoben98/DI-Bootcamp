// // Exercise 1: Sum Elements

// function sum(numsArray) {
//   let sum = 0;
//   for (let i = 0; i < numsArray.length; i++) {
//     sum += numsArray[i];
//   }
//   return sum;
// }
// console.log(sum([2, 5, 10]));

// // Exercise 2 : Remove Duplicates

// const removeDuplicates = (arr) => {
//   return [...new Set(arr)];
// };

// const array = [1, 2, 3, 4, 4, 5, 6, 6, 7];
// const result = removeDuplicates(array);
// console.log(result);

// // Exercise 3 : Remove Certain Values

// const removeFalsyValues = (arr) => {
//   return arr.filter(Boolean);
// };

// const array = [NaN, 0, 15, false, -22, "", undefined, 47, null];
// const result = removeFalsyValues(array);

// console.log(result);

// // Exercise 4 : Repeat Please !

// const repeat = (str, n = 1) => {
//   let result = "";
//   for (let i = 0; i < n; i++) {
//     result += str;
//   }
//   return result;
// };

// console.log(repeat("Ha!", 3));

// // Exercise 5 : Turtle & Rabbit
// const startLine = "     ||<- Start line";
// let turtle = "🐢";
// let rabbit = "🐇";
// turtle = turtle.trim().padEnd(9, "=");

// console.log(startLine);
// console.log(turtle);
// console.log(rabbit);
