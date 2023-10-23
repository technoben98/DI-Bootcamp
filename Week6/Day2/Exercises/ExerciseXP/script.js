// 🌟 Exercise 1 : Change The Article

// const h1 = document.querySelector("article h1");
// console.log(h1);

// let article = document.getElementsByTagName("article");
// article[0].removeChild(article[0].lastElementChild);

// const h2 = document.querySelector("h2");
// // console.log(h2);
// h2.addEventListener("click", function () {
//   h2.style.backgroundColor = "red";
// });

// const h3 = document.querySelector("h3");
// h3.addEventListener("click", function () {
//   h3.style.display = "none";
// });

// const button = document.querySelector("button");
// button.addEventListener("click", function () {
//   article[0].style.fontWeight = "bold";
// });

// h1.addEventListener("mouseover", function () {
//   size = Math.random() * 100;
//   size = Math.trunc(size);
//   h1.style.fontSize = `${size}px`;
// });

// const allParagraphs = document.querySelectorAll("p");
// const secondParagraph = allParagraphs[1];
// console.log(secondParagraph);
// secondParagraph.addEventListener("mouseover", function () {
//   secondParagraph.style.opacity = "0";
//   secondParagraph.style.transition = "opacity 0.5s";
// });

// 🌟 Exercise 2 : Work With Forms

// const form = document.querySelector("form");
// console.log(form);

// const fnameById = document.querySelector("#fname");
// const lnameById = document.querySelector("#lname");
// const fnameByName = document.getElementsByName("firstname");
// const lnameByName = document.getElementsByName("lastname");

// console.log(fnameById);
// console.log(lnameById);
// console.log(fnameByName);
// console.log(lnameByName);

// form.addEventListener("submit", function (event) {
//   event.preventDefault();

//   const firstNameValue = fnameById.value.trim();
//   const lastNameValue = lnameById.value.trim();

//   if (firstNameValue === "" || lastNameValue === "") {
//     alert("Please fill in all fields.");
//     return;
//   }

//   const outputList = document.querySelector("ul");
//   const firstNameLi = document.createElement("li");
//   const lastNameLi = document.createElement("li");

//   firstNameLi.textContent = firstNameValue;
//   lastNameLi.textContent = lastNameValue;

//   outputList.appendChild(firstNameLi);
//   outputList.appendChild(lastNameLi);
// });

// 🌟 Exercise 3 : Transform The Sentence

// let allBoldItems;

// function getBoldItems() {
//   const sentence = document.querySelector("p");
//   allBoldItems = sentence.querySelectorAll("strong");
// }

// function highlight() {
//   for (let i = 0; i < allBoldItems.length; i++) {
//     allBoldItems[i].style.color = "blue";
//   }
// }

// function returnItemsToDefault() {
//   for (let i = 0; i < allBoldItems.length; i++) {
//     allBoldItems[i].style.color = "black";
//   }
// }

// getBoldItems();

// const sentence = document.querySelector("p");
// sentence.addEventListener("mouseover", highlight);
// sentence.addEventListener("mouseout", returnItemsToDefault);

// 🌟 Exercice 4 : Volume Of A Sphere

const form = document.querySelector("#MyForm");

form.addEventListener("submit", function (event) {
  event.preventDefault();

  const radiusInput = document.querySelector("#radius");
  const volumeInput = document.querySelector("#volume");

  const radius = parseFloat(radiusInput.value);
  const volume = calculateSphereVolume(radius);

  volumeInput.value = volume.toFixed(2);
});

function calculateSphereVolume(radius) {
  const volume = (4 / 3) * Math.PI * Math.pow(radius, 3);
  return volume;
}
