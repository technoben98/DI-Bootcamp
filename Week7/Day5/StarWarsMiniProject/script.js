const randomBtn = document.getElementById("button");
const nameElement = document.getElementById("name");
const heightElement = document.getElementById("height");
const genderElement = document.getElementById("gender");
const birthYearElement = document.getElementById("birthYear");
const homeWorldElement = document.getElementById("homeWorld");

randomBtn.addEventListener("click", getRandomCharacter);

function getRandomCharacter() {
  updateWithLoading();

  const randomNumber = Math.floor(Math.random() * 88 + 1);
  const apiUrl = "https://swapi.dev/api/people/" + randomNumber + "/";

  fetch(apiUrl)
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      const character = data;

      nameElement.textContent = `Name: ${character.name}`;
      heightElement.textContent = `Height: ${character.height}`;
      genderElement.textContent = `Gender: ${character.gender}`;
      birthYearElement.textContent = `Birth Year: ${character.birth_year}`;

      getHomeWorld(character.homeworld);
    })
    .catch((error) => {
      nameElement.textContent = "Error fetching data";
      console.log(error);
    });
}

function getHomeWorld(planetUrl) {
  fetch(planetUrl)
    .then((response) => response.json())
    .then((data) => {
      homeWorldElement.textContent = `Planet: ${data.name}`;
    })
    .catch((error) => {
      homeWorldElement.textContent = "Unknown";
      console.error(error);
    });
}
function updateWithLoading() {
  nameElement.innerHTML =
    '<i class="fa-solid fa-spinner fa-spin fa-2xl"></i> <p>Loading...</p>';
  heightElement.innerText = "";
  genderElement.innerText = "";
  birthYearElement.innerText = "";
  homeWorldElement.innerText = "";
}
