// 🌟 Exercise 1 : HTML Form

// When you click the Send button and the form is submitted with a GET method, the sent data will appear in the URL of the page. The form inputs will be appended as query parameters to the URL.

// 🌟 Exercise 2 : HTML Form #2

// When you submit the form with a POST method, the sent data will not appear directly on the page. Instead, it will be sent to the server as part of the request payload. You can view the sent data in the Network Tab of your browser's Developer Tools.

// 🌟 Exercise 3 : JSON Mario

const marioGame = {
  detail: "An amazing game!",
  characters: {
    mario: {
      description: "Small and jumpy. Likes princesses.",
      height: 10,
      weight: 3,
      speed: 12,
    },
    bowser: {
      description: "Big and green, Hates princesses.",
      height: 16,
      weight: 6,
      speed: 4,
    },
    princessPeach: {
      description: "Beautiful princess.",
      height: 12,
      weight: 2,
      speed: 2,
    },
  },
};

const json = JSON.stringify(marioGame, null, 2);
console.log(json);
