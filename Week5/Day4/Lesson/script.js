// Exercise 1

// console.log("Hello world")
// let addressNumber = 15;
// let addressStreet = "BenYehuda";
// let country = "Israel";
// let globalAddress = "I live in " + addressStreet + " " + addressNumber + ", in " + country;
// let betterGlobalAddress = `I live in ${addressStreet} ${addressNumber}, in ${country}`
// console.log(globalAddress)

// Exercise 2
// let birthYear = 1998;
// let futureYear = 2024;
// console.log(`I will be ${futureYear - birthYear} in ${futureYear}`)

// let age = prompt('How old are you?', 20);
// alert(`You are ${age} years old!`);

// Exercise 3

// let pets = ["cat", "dog", "fish", "rabbit", "cow"]
// console.log(pets[1])
// pets.splice(1, 1)
// console.log(pets[3])
// pets.push("horse")
// console.log(pets.length)

// Exercise 4

// let userAge = prompt("Your age?")
// if (userAge < 18) {
//     alert("Sorry, you are too young to drive this car. Powering off")
// } else if (userAge == 18){
//     alert("Congratulations on your first year of driving. Enjoy the ride!")
// } else if (userAge > 18) {
//     alert("Powering On. Enjoy the ride!")
// } else {
//     alert("Wrong format!")
// }

// Exercise 5

// for (i = 0; i < 16; i++){

//     if (i % 2 == 0){
//         console.log(`${i} is even`)
//     } else {
//         console.log(`${i} is odd`)
//     }
// };

// Exercise 6

let names= ["john", "sarah", 23, "Rudolf", 34];
for(let i of names){
    if (typeof(i) == 'string'){
        if(i[0] == i[0].toUpperCase()){
            console.log(i)
        }else{
            i = i[0].toUpperCase() + i.slice(1)
            i[0] = i[0].toUpperCase()
            console.log(i)
        }
    } else {
        continue
    }
}