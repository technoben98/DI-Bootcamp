// 🌟 Exercise 1 : Comparison

// function compareToTen(num) {
//   return new Promise((resolve, reject) => {
//     if (num <= 10) {
//       resolve(`${num} is less than or equal to 10`);
//     } else {
//       reject(`${num} is greater than 10`);
//     }
//   });
// }

// // Test cases
// compareToTen(15)
//   .then((result) => console.log(result))
//   .catch((error) => console.log(error));

// compareToTen(8)
//   .then((result) => console.log(result))
//   .catch((error) => console.log(error));

// 🌟 Exercise 2 : Promises

// function delay(time) {
//   return new Promise((resolve) => {
//     setTimeout(() => {
//       resolve("success");
//     }, time);
//   });
// }

// delay(4000)
//   .then((result) => {
//     console.log(result);
//   })
//   .catch((error) => {
//     console.log(error);
//   });

// 🌟 Exercise 3 : Resolve & Reject

// const promise1 = Promise.resolve(3);
// const promise2 = Promise.reject("Boo!");

// promise1
//   .then((result) => console.log(result))
//   .catch((error) => console.log(error));

// promise2
//   .then((result) => console.log(result))
//   .catch((error) => console.log(error));
