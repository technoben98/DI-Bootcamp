// // Exercise 1 : Dog Age To Human Years

// const data = [
//   {
//     name: "Butters",
//     age: 3,
//     type: "dog",
//   },
//   {
//     name: "Cuty",
//     age: 5,
//     type: "rabbit",
//   },
//   {
//     name: "Lizzy",
//     age: 6,
//     type: "dog",
//   },
//   {
//     name: "Red",
//     age: 1,
//     type: "cat",
//   },
//   {
//     name: "Joey",
//     age: 3,
//     type: "dog",
//   },
//   {
//     name: "Rex",
//     age: 10,
//     type: "dog",
//   },
// ];

// let sum1 = 0;

// for (let i = 0; i < data.length; i++) {
//   if (data[i].type === "dog") {
//     sum1 += data[i].age * 7; // 1 dog year equals 7 human years
//   }
// }

// console.log(sum1);

// const sum = data.reduce((acc, obj) => {
//   if (obj.type === "dog") {
//     return acc + obj.age * 7; // 1 dog year equals 7 human years
//   }
//   return acc;
// }, 0);

// console.log(sum);

// // Exercise 2 : Email
// const userEmail3 = " cannotfillemailformcorrectly@gmail.com "
//   .trim()
//   .replace(/\s+/g, "");
// console.log(userEmail3);

// // Exercise 3 : Employees #3

// const users = [
//   { firstName: "Bradley", lastName: "Bouley", role: "Full Stack Resident" },
//   { firstName: "Chloe", lastName: "Alnaji", role: "Full Stack Resident" },
//   { firstName: "Jonathan", lastName: "Baughn", role: "Enterprise Instructor" },
//   { firstName: "Michael", lastName: "Herman", role: "Lead Instructor" },
//   { firstName: "Robert", lastName: "Hajek", role: "Full Stack Resident" },
//   { firstName: "Wes", lastName: "Reid", role: "Instructor" },
//   { firstName: "Zach", lastName: "Klabunde", role: "Instructor" },
// ];

// const usersObject = users.reduce((obj, user) => {
//   const fullName = `${user.firstName} ${user.lastName}`;
//   obj[fullName] = user.role;
//   return obj;
// }, {});

// console.log(usersObject);

// // Exercise 4 : Array To Object

// const letters = ["x", "y", "z", "z"];

// const countForLoop = {};
// for (let i = 0; i < letters.length; i++) {
//   const letter = letters[i];
//   countForLoop[letter] = (countForLoop[letter] || 0) + 1;
// }
// console.log(countForLoop);

// const countReduce = letters.reduce((acc, letter) => {
//   acc[letter] = (acc[letter] || 0) + 1;
//   return acc;
// }, {});
// console.log(countReduce);

// // Exercise 1 : Menu

// const menu = [
//   {
//     type: "starter",
//     name: "Houmous with Pita",
//   },
//   {
//     type: "starter",
//     name: "Vegetable Soup with Houmous peas",
//   },
//   {
//     type: "dessert",
//     name: "Chocolate Cake",
//   },
// ];

// const hasDessert = menu.some((item) => item.type === "dessert");
// console.log(hasDessert);

// const allStarters = menu.every((item) => item.type === "starter");
// console.log(allStarters);

// const hasMainCourse = menu.some((item) => item.type === "main");
// if (!hasMainCourse) {
//   const mainCourse = { type: "main", name: "Grilled Salmon" };
//   menu.push(mainCourse);
// }
// console.log(menu);

// const vegetarian = ["vegetable", "houmous", "eggs", "vanilla", "potatoes"];

// menu.forEach((item) => {
//   const isVegetarian = vegetarian.some((ingredient) =>
//     item.name.toLowerCase().includes(ingredient)
//   );
//   item.vegetarian = isVegetarian;
// });
// console.log(menu);

// // Exercise 2 : Chop Into Chunks

// function string_chop(str, length) {
//   const chunks = [];
//   let index = 0;

//   while (index < str.length) {
//     chunks.push(str.slice(index, index + length));
//     index += length;
//   }

//   return chunks;
// }

// console.log(string_chop("developers", 2));

// // Exercise 3 : You Said String ?

// function search_word(sentence, word) {
//   const regex = new RegExp(`\\b${word}\\b`, "gi");
//   const matches = sentence.match(regex);
//   const count = matches ? matches.length : 0;
//   return `'${word}' was found ${count} times.`;
// }

// console.log(search_word("The quick brown fox", "fox"));
// console.log(search_word("The fox quick fox brown fox fox", "fox"));

// // Exercise 4 : Reverse Array

// function reverseArray(arr) {
//   let start = 0;
//   let end = arr.length - 1;

//   while (start < end) {
//     let temp = arr[start];
//     arr[start] = arr[end];
//     arr[end] = temp;
//     start++;
//     end--;
//   }

//   return arr;
// }

// console.log(reverseArray([1, 2, 3, 4, 5]));
// console.log(reverseArray([1, 2]));
// console.log(reverseArray([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]));
