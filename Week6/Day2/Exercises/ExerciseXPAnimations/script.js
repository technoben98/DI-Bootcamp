// 🌟 Exercise 1: Timer

// // Part 1
// setTimeout(function () {
//   alert("Hello World");
// }, 2000);

// // Part 2
// setTimeout(function () {
//   const container = document.querySelector("#container");
//   const paragraph = document.createElement("p");
//   paragraph.textContent = "Hello World";
//   container.appendChild(paragraph);
// }, 2000);

// Part 3
// const container = document.querySelector("#container");
// const button = document.querySelector("#clear");
// let intervalId;
// let paragraphCount = 0;

// function addParagraph() {
//   const paragraph = document.createElement("p");
//   paragraph.textContent = "Hello World";
//   container.appendChild(paragraph);
//   paragraphCount++;

//   if (paragraphCount >= 5) {
//     clearInterval(intervalId);
//   }
// }

// intervalId = setInterval(addParagraph, 2000);

// button.addEventListener("click", function () {
//   clearInterval(intervalId);
// });

// 🌟 Exercise 2 : Move The Box

function myMove() {
  const container = document.getElementById("container");
  const animate = document.getElementById("animate");
  let position = 0;
  const containerWidth = container.offsetWidth;
  const animateWidth = animate.offsetWidth;

  const intervalId = setInterval(() => {
    position++;
    animate.style.left = position + "px";

    if (position >= containerWidth - animateWidth) {
      clearInterval(intervalId);
    }
  }, 1);
}
