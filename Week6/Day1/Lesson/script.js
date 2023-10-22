// Exercise 1

// function familyAge(myAge){
//     let momAge = myAge * 2;
//     let dadAge = momAge * 1.2;
//     console.log(`My Mother age is ${momAge} and Daddy's age is ${dadAge}.`);
// }

// familyAge(25);

// Exercise 2

// function getMomAge(myAge){
//     let momAge = myAge*2;
//     return momAge;
// }

// console.log(getMomAge(30))

// Exercise 3

const div = document.getElementById("container") //1
const alsoDiv = document.querySelector("#container") //2
const alsoDiv1 = document.querySelector("div")
const body = document.body
console.log(body.firstElementChild)

// const ulElements = document.getElementsByClassName("list")
// for (let ulElement of ulElements){
//     const liElements = ulElement.getElementsByTagName("li")
//     for(const li of liElements){
//         console.log(li.textContent)
//     }
// }

// const liElements = document.querySelectorAll("ul.list li")
// console.log(liElements)
// for (let li of liElements){
//     console.log(li.textContent)
// }


const ulElements = document.getElementsByClassName("list")
console.log(ulElements)
for (let ul of ulElements){
    console.log(ul.firstElementChild.textContent)
}