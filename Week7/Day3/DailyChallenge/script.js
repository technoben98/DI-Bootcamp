// 1st Daily Challenge

// function makeAllCaps(words) {
//   return new Promise((resolve, reject) => {
//     if (Array.isArray(words)) {
//       const allStrings = words.every((word) => typeof word === "string");
//       if (allStrings) {
//         resolve(words.map((word) => word.toUpperCase()));
//       } else {
//         reject("Array contains non-string element(s).");
//       }
//     } else {
//       reject("Argument is not an array.");
//     }
//   });
// }

// function sortWords(words) {
//   return new Promise((resolve, reject) => {
//     if (Array.isArray(words)) {
//       if (words.length > 4) {
//         resolve(words.sort());
//       } else {
//         reject("Array length is not greater than 4.");
//       }
//     } else {
//       reject("Argument is not an array.");
//     }
//   });
// }

// // Test cases
// makeAllCaps([1, "pear", "banana"])
//   .then((arr) => sortWords(arr))
//   .then((result) => console.log(result))
//   .catch((error) => console.log(error));

// makeAllCaps(["apple", "pear", "banana"])
//   .then((arr) => sortWords(arr))
//   .then((result) => console.log(result))
//   .catch((error) => console.log(error));

// makeAllCaps(["apple", "pear", "banana", "melon", "kiwi"])
//   .then((arr) => sortWords(arr))
//   .then((result) => console.log(result))
//   .catch((error) => console.log(error));

// 2nd Daily Challenge

const morse = `{
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
  }`;

function toJs() {
  return new Promise((resolve, reject) => {
    const morseJS = JSON.parse(morse);
    if (Object.keys(morseJS).length === 0) {
      reject("Morse JavaScript object is empty.");
    } else {
      resolve(morseJS);
    }
  });
}

function toMorse(morseJS) {
  return new Promise((resolve, reject) => {
    const word = prompt("Enter a word or sentence:");
    const translation = [];
    [...word].forEach((char) => {
      if (morseJS[char.toLowerCase()]) {
        translation.push(morseJS[char.toLowerCase()]);
      } else {
        reject(
          `Character "${char}" doesn't exist in the Morse JavaScript object.`
        );
      }
    });
    resolve(translation);
  });
}

function joinWords(morseTranslation) {
  const result = morseTranslation.join("<br>");
  document.getElementById("morseOutput").innerHTML = result;
}

toJs()
  .then((morseJS) => toMorse(morseJS))
  .then((morseTranslation) => joinWords(morseTranslation))
  .catch((error) => console.log(error));
