// // Exercise 1 : Calculate The Tip

// function calculateTip() {
//   const billAmount = document.getElementById("billamt").value;
//   const serviceQuality = document.getElementById("serviceQual").value;
//   const numberOfPeople = document.getElementById("peopleamt").value;

//   if (serviceQuality === "0" || billAmount === "") {
//     alert("Please enter the bill amount and select a service quality");
//     return;
//   }

//   if (numberOfPeople === "" || numberOfPeople < 1) {
//     document.getElementById("each").style.display = "none";
//     numberOfPeople = 1;
//   } else {
//     document.getElementById("each").style.display = "inline";
//   }

//   const total = (billAmount * serviceQuality) / numberOfPeople;
//   const roundedTotal = total.toFixed(2);

//   document.getElementById("totalTip").style.display = "block";
//   document.getElementById("tip").textContent = roundedTotal;
// }

// document.getElementById("calculate").addEventListener("click", calculateTip);

// Exercise 2 : Validate The Email

// document
//   .getElementById("emailForm")
//   .addEventListener("submit", function (event) {
//     event.preventDefault();
//     const emailInput = document.getElementById("email");
//     const email = emailInput.value;

//     if (validateEmail(email)) {
//       alert("Valid email address");
//     } else {
//       alert("Invalid email address");
//     }
//   });

// function validateEmail(email) {
//   const atIndex = email.indexOf("@");
//   const dotIndex = email.lastIndexOf(".");

//   if (atIndex < 1 || dotIndex < atIndex + 2 || dotIndex + 2 >= email.length) {
//     return false;
//   }

//   return true;
// }

// Exercise 3 : Get The User’s Geolocation Coordinates

function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else {
    alert("Geolocation is not supported by this browser.");
  }
}

function showPosition(position) {
  const latitude = position.coords.latitude;
  const longitude = position.coords.longitude;
  document.getElementById(
    "output"
  ).innerHTML = `Latitude: ${latitude}<br>Longitude: ${longitude}`;
}
