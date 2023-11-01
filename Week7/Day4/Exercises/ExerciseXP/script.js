// // 🌟 Exercise 1 : Giphy API

// fetch(
//   "https://api.giphy.com/v1/gifs/search?q=hilarious&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My"
// )
//   .then((response) => {
//     if (!response.ok) {
//       throw new Error(`Failed to fetch data. Status: ${response.status}`);
//     }
//     return response.json();
//   })
//   .then((data) => {
//     console.log(data);
//   })
//   .catch((error) => {
//     console.log(error);
//   });

// // 🌟 Exercise 2 : Giphy API

// fetch(
//   "https://api.giphy.com/v1/gifs/search?q=sun&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My&limit=10&offset=2"
// )
//   .then((response) => {
//     if (!response.ok) {
//       throw new Error(`Failed to fetch data. Status: ${response.status}`);
//     }
//     return response.json();
//   })
//   .then((data) => {
//     console.log(data);
//   })
//   .catch((error) => {
//     console.log(error);
//   });

// // 🌟 Exercise 3 : Async Function

// async function fetchStarWarsData() {
//   try {
//     const response = await fetch("https://www.swapi.tech/api/starships/9/");
//     if (!response.ok) {
//       throw new Error(`Failed to fetch data. Status: ${response.status}`);
//     }
//     const data = await response.json();
//     console.log(data.result);
//   } catch (error) {
//     console.log(error);
//   }
// }

// fetchStarWarsData();

// 🌟 Exercise 4: Analyze

function resolveAfter2Seconds() {
  //function returns a Promise that resolves after a 2-second timeout.

  return new Promise((resolve) => {
    setTimeout(() => {
      resolve("resolved");
    }, 2000);
  });
}

async function asyncCall() {
  // async function logs "calling" to the console.
  console.log("calling"); //console.log without "await" will print "calling" before 2 sec timeout from previous func.
  let result = await resolveAfter2Seconds(); //await keyword is used to wait for the Promise returned by resolveAfter2Seconds() to resolve.
  console.log(result);
}

asyncCall(); //it gives us first calling and after this resolved.
