const API_KEY = "hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My";
const searchInput = document.getElementById("searchInput");
const searchBtn = document.getElementById("searchBtn");
const gifContainer = document.getElementById("gifContainer");
const deleteAllBtn = document.getElementById("deleteAllBtn");

searchBtn.addEventListener("click", fetchRandomGif);
deleteAllBtn.addEventListener("click", deleteAllGifs);

function fetchRandomGif() {
  const searchQuery = searchInput.value;
  const url = `https://api.giphy.com/v1/gifs/random?api_key=${API_KEY}&tag=${searchQuery}`;

  fetch(url)
    .then((response) => response.json())
    .then((data) => {
      const gifUrl = data.data.images.original.url;
      const gifElement = createGifElement(gifUrl);
      gifContainer.appendChild(gifElement);
    })
    .catch((error) => console.error(error));

  searchInput.value = "";
}

function createGifElement(gifUrl) {
  const gifElement = document.createElement("div");
  const gifImg = document.createElement("img");
  const deleteBtn = document.createElement("button");

  gifImg.src = gifUrl;
  deleteBtn.textContent = "DELETE";

  deleteBtn.addEventListener("click", () => {
    gifElement.remove();
  });

  gifElement.appendChild(gifImg);
  gifElement.appendChild(deleteBtn);

  return gifElement;
}

function deleteAllGifs() {
  gifContainer.innerHTML = "";
}
