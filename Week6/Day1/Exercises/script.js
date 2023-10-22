// 🌟 Exercise 1 : Find The Numbers Divisible By 23

// function displayNumberDivisible(divisor){
//     let sum = 0;
//     for (let i = 0; i < 500; i++){
//         if (i%divisor ==0){
//             console.log(i)
//             sum += i;
//         }
//     }
//     console.log(sum)
// };

// displayNumberDivisible(3);

// 🌟 Exercise 2 : Shopping List

// const stock = { 
//     "banana": 6, 
//     "apple": 0,
//     "pear": 12,
//     "orange": 32,
//     "blueberry":1
// }  

// const prices = {    
//     "banana": 4, 
//     "apple": 2, 
//     "pear": 1,
//     "orange": 1.5,
//     "blueberry":10
// } 

// shoppingList = ["banana", "orange", "apple"]

// function myBill(){
//     let sum = 0;
//     for(item in shoppingList){
//         for(item in stock){
//             if (stock[item] !=0){
//                 sum+= prices[item];
//                 stock[item]--;
//             };
//         };
//         return sum;
//     }
// };

// console.log(myBill())

// 🌟 Exercise 3: What’s In My Wallet ?

// function changeEnough(itemPrice, amountOfChange){
//     let totalChange = 0.25 * amountOfChange[0] + 0.10 * amountOfChange[1] + 0.05 * amountOfChange[2] + 0.01 * amountOfChange[3];
//     if(totalChange >= itemPrice){
//         return true;
//     } else {
//         return false;
//     }
// }
// console.log(changeEnough(4.25, [25, 20, 5, 0]));
// console.log(changeEnough(14.11, [2, 100, 0, 0]));
// console.log(changeEnough(0.75, [0, 0, 20, 5]));


// 🌟 Exercise 4 : Vacations Costs

// function hotelCost(nights) {
//     return nights * 140;
// }
// function planeRideCost(destination) {
//     if (destination === "London") {
//       return 183;
//     } else if (destination === "Paris") {
//       return 220;
//     } else {
//       return 300;
//     }
// }
// function rentalCarCost(days) {
//     if (days < 10) {
//       return days * 40;
//     } else if (days >= 10) {
//       return days * (40 * 0.95);
//     }
// }

// function totalVacantionCost() {
//     let nights, destination, days;
//     while(true){
//         nights = prompt("How many nights do you need?");
//         parseInt(nights)
//         if (nights > 0){
//             break
//         } else {
//             continue
//         }
//     }
//     while(typeof(destination) != "string"){
//         destination = prompt("Where are you going?");
//     }
    
//     while(true){
//         days = prompt("How many days do you need a car?");
//         if (days > 0){
//             break
//         } else { 
//             continue
//         }
//     }
    
//     let hotel = hotelCost(nights);
//     let tickets = planeRideCost(destination);
//     let car = rentalCarCost(days);
    
//     return `The hotel cost: $${hotel}, the plane tickets cost: $${tickets}, and the car cost: $${car}`;
// }
// alert(totalVacantionCost())


// 🌟 Exercise 5 : Users

// let div = document.getElementById("container");
// console.log(div);

// let lis = div.getElementsByTagName("li");
// for (let i = 0; i < lis.length; i++) {
//   if (lis[i].textContent === "Pete") {
//     lis[i].textContent = "Richard";
//   }
// }

// let secondUl = div.getElementsByClassName("list")[1];
// let secondLi = secondUl.getElementsByTagName("li")[1];
// secondUl.removeChild(secondLi);


// let lists = div.getElementsByClassName("list");
// for (let i = 0; i < lists.length; i++) {
//   let firstLi = lists[i].getElementsByTagName("li")[0];
//   firstLi.textContent = "Mike";
// }

// let uls = div.getElementsByTagName("ul");
// for (let i = 0; i < uls.length; i++) {
//   uls[i].classList.add("student_list");
// }

// let firstUl = uls[0];
// firstUl.classList.add("university");
// firstUl.classList.add("attendance");

// div.style.backgroundColor = "lightblue";
// div.style.padding = "10px";

// for (let i = 0; i < lis.length; i++) {
//     if (lis[i].textContent === "Dan") {
//       lis[i].style.display = "none";
//     }
//   }

// let richardLi = firstUl.getElementsByTagName("li")[1];
// richardLi.style.border = "1px solid black";

// document.body.style.fontSize = "16px";

// let users = div.textContent.trim().split(/\n/);
// let x = users[1].trim();
// let y = users[2].trim();
// if (div.style.backgroundColor === "lightblue") {
//   alert("Hello " + x + " and " + y);
// }

// 🌟 Exercise 6 : Change The Navbar

// let div = document.getElementById("navBar")
// div.setAttribute("id", "socialNetworkNavigation")

// let ul = document.querySelector("#socialNetworkNavigation ul")
// let newLi = document.createElement("li");
// let textNode = document.createTextNode("Logout");
// newLi.appendChild(textNode);
// ul.appendChild(newLi);

// let firstLi = ul.firstElementChild;
// let lastLi = ul.lastElementChild;

// console.log(firstLi.textContent);
// console.log(lastLi.textContent);


// 🌟 Exercise 7 : My Book List

const section = document.getElementsByClassName("listBooks")[0]

let allBooks = [
    {
        title: "Harry Potter",
        author: "J.K. Rowling",
        image: "https://image.smythstoys.com/original/desktop/191077_7.jpg",
        alreadyRead: false
    },
    {
        title: "Wiedzmin",
        author: "Andrzej Sapkowski",
        image: "https://www.expatspoland.com/wp-content/uploads/2019/04/the_witcher_books_order.jpg",
        alreadyRead: true
    }
  ];

for (let i = 0; i < allBooks.length; i++) {
    const bookDiv = document.createElement("div");
    
    const titleP = document.createElement("p");
    titleP.textContent = `Title: ${allBooks[i].title}`;
    bookDiv.appendChild(titleP);
    
    const authorP = document.createElement("p");
    authorP.textContent = `Author: ${allBooks[i].author}`;
    bookDiv.appendChild(authorP);
    
    const image = document.createElement("img");
    image.src = allBooks[i].image;
    image.style.width = "100px";
    bookDiv.appendChild(image);
    
    if (allBooks[i].alreadyRead) {
      bookDiv.style.color = "red";
    }
    
    section.appendChild(bookDiv);
}