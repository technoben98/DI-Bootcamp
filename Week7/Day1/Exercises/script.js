// 🌟 Exercise 1 : Location

// const person = {
//   name: "John Doe",
//   age: 25,
//   location: {
//     country: "Canada",
//     city: "Vancouver",
//     coordinates: [49.2827, -123.1207],
//   },
// };

// const { //destructuring object to values
//   name,
//   location: {
//     country,
//     city,
//     coordinates: [lat, lng],
//   },
// } = person;

// console.log(
//   `I am ${name} from ${city}, ${country}. Latitude(${lat}), Longitude(${lng})`
// ); //using all of values to create string with

// 🌟 Exercise 2: Display Student Info

// function displayStudentInfo(objUser) {
//   const { first, last } = objUser;
//   return `Your full name is ${first} ${last}`;
// }

// console.log(displayStudentInfo({ first: "Elie", last: "Schoppik" }));

// 🌟 Exercise 3: User & Id

// const users = { user1: 18273, user2: 92833, user3: 90315 };

// const usersArray = Object.entries(users);
// console.log(usersArray);

// const modifiedArray = usersArray.map(([key, value]) => [key, value * 2]);
// console.log(modifiedArray);

// 🌟 Exercise 4 : Person Class

// class Person {
//   constructor(name) {
//     this.name = name;
//   }
// }

// const member = new Person("John");
// console.log(typeof member); // type of member is object

// 🌟 Exercise 5 : Dog Class

// class Dog {
//   constructor(name) {
//     this.name = name;
//   }
// }

// // 2
// class Labrador extends Dog {
//   constructor(name, size) {
//     super(name);
//     this.size = size;
//   }
// }
// Answer: I choose second one because there we have right constructor, we use super to take parameters from parent class and init variable size by useing key word "this"

// 🌟 Exercise 6 : Challenges

// 1
// [2] === [2]
// {} === {}
//they are always be false

// 2

// const object1 = { number: 5 }; // key:value is number:5
// const object2 = object1; // object2 just a link to object1 in memory
// const object3 = object2; // object3 takes params from object2 that takes param from object1
// const object4 = { number: 5 }; // object4 have a private params

// object1.number = 4; //we changing value for object1 and because of object2 and 3 takes their values from object1 they will take 4 after this line
// console.log(object2.number); // 4
// console.log(object3.number); // 4
// console.log(object4.number); // 5

// class Animal {
//   constructor(name, type, color) {
//     this.name = name;
//     this.type = type;
//     this.color = color;
//   }
// }

// class Mamal extends Animal {
//   sound(sound) {
//     return `${sound} I'm a ${this.type}, named ${this.name} and I'm ${this.color}.`;
//   }
// }
// const farmerCow = new Mamal("Lily", "cow", "brown and white");
// console.log(farmerCow.sound("Moooo"));
