// Exercise 1

// const people = ["Greg", "Mary", "Devon", "James"];
// people.splice(0, 1);
// people [2] = "Jason";
// people.push("Dmitriy");

// console.log(people.indexOf("Mary"));
// const people2 = people.slice(1);
// console.log(people2);

// console.log(people.indexOf("Foo"));

// let last = people[people.length - 1];
// console.log(last);

// for (let i = 0; i < people.length; i++){
//     console.log(people[i]);
// };

// for (let i = 0; i < people.length; i++){
//     console.log(people[i]);
//     if (people[i] == "Devon"){
//         break;
//     };
// };

// Exercise 2

// const colors = ["violet", "red", "black", "aqua"];
// const suffixes = ["st", "nd", "rd", "th"];
// for (let i = 0; i < colors.length; i++){
//     console.log(`My ${i+1+suffixes[i]} choice is ${colors[i]}.`);
// };

// Exercise 3
// console.log("start");
// number = prompt("Put your number");
// console.log(typeof(number));
// while (number < 10){
//     number = prompt("Put your number");
// };

// Exercise 4

// const building = {
//     numberOfFloors: 4,
//     numberOfAptByFloor: {
//         firstFloor: 3,
//         secondFloor: 4,
//         thirdFloor: 9,
//         fourthFloor: 2,
//     },
//     nameOfTenants: ["Sarah", "Dan", "David"],
//     numberOfRoomsAndRent:  {
//         sarah: [3, 990],
//         dan:  [4, 1000],
//         david: [1, 500],
//     },
// };

// console.log(building.numberOfFloors);
// console.log(building.numberOfAptByFloor.firstFloor + building.numberOfAptByFloor.thirdFloor);
// console.log(`${building.nameOfTenants[1]} has ${building.numberOfRoomsAndRent.dan[0]} rooms.`);

// let sumOfRent = building.numberOfRoomsAndRent.sarah[1]+building.numberOfRoomsAndRent.david[1];
// if(building.numberOfRoomsAndRent.dan[1] < sumOfRent){
//     building.numberOfRoomsAndRent.dan[1]+=200;
// };
// console.log(building.numberOfRoomsAndRent.dan[1]);

// Exercise 5

// const family = {
//     person1: 'Greg',
//     person2: 'Ben',
//     person3: 'Dan',
//     person4: 'David',
// };

// for (key in family){
//     console.log(key);
//     console.log(family[key]);
// };

// Execrise 6

// const details = {
//     my: 'name',
//     is: 'Rudolf',
//     the: 'raindeer'
// };
// let above = '';
// for(key in details){
//     above += key + " " + details[key] + " ";
// };
// console.log(above);

// Exercise 7

// const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

// names.sort();
// let secret = ""
// for (let i = 0; i < names.length; i++){
//     secret += names[i][0];
// };
// console.log(secret);