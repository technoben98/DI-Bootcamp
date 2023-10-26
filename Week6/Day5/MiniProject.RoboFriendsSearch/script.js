const robots = [
  {
    id: 1,
    name: "Leanne Graham",
    username: "Bret",
    email: "Sincere@april.biz",
    image: "https://robohash.org/1?200x200",
  },
  {
    id: 2,
    name: "Ervin Howell",
    username: "Antonette",
    email: "Shanna@melissa.tv",
    image: "https://robohash.org/2?200x200",
  },
  {
    id: 3,
    name: "Clementine Bauch",
    username: "Samantha",
    email: "Nathan@yesenia.net",
    image: "https://robohash.org/3?200x200",
  },
  {
    id: 4,
    name: "Patricia Lebsack",
    username: "Karianne",
    email: "Julianne.OConner@kory.org",
    image: "https://robohash.org/4?200x200",
  },
  {
    id: 5,
    name: "Chelsey Dietrich",
    username: "Kamren",
    email: "Lucio_Hettinger@annie.ca",
    image: "https://robohash.org/5?200x200",
  },
  {
    id: 6,
    name: "Mrs. Dennis Schulist",
    username: "Leopoldo_Corkery",
    email: "Karley_Dach@jasper.info",
    image: "https://robohash.org/6?200x200",
  },
  {
    id: 7,
    name: "Kurtis Weissnat",
    username: "Elwyn.Skiles",
    email: "Telly.Hoeger@billy.biz",
    image: "https://robohash.org/7?200x200",
  },
  {
    id: 8,
    name: "Nicholas Runolfsdottir V",
    username: "Maxime_Nienow",
    email: "Sherwood@rosamond.me",
    image: "https://robohash.org/8?200x200",
  },
  {
    id: 9,
    name: "Glenna Reichert",
    username: "Delphine",
    email: "Chaim_McDermott@dana.io",
    image: "https://robohash.org/9?200x200",
  },
  {
    id: 10,
    name: "Clementina DuBuque",
    username: "Moriah.Stanton",
    email: "Rey.Padberg@karina.biz",
    image: "https://robohash.org/10?200x200",
  },
];

const displayCards = (array) => {
  const container = document.querySelector("#container");
  container.innerHTML = "";
  if (array.length === 0) {
    const message = document.createElement("p");
    message.style.fontSize = "30px";
    message.textContent = "Sorry, we cant find this robot!";
    container.appendChild(message);
  } else {
    array.forEach((robot) => {
      let divCard = document.createElement("div");
      divCard.classList.add("card");
      divCard.id = robot.id;

      let imageOfRobots = document.createElement("div");
      imageOfRobots.classList.add("roboImg");
      let img = document.createElement("img");
      img.setAttribute("src", robot.image);
      imageOfRobots.append(img);
      divCard.appendChild(imageOfRobots);

      let roboName = document.createElement("h2");
      roboName.append(document.createTextNode(robot.name));
      divCard.appendChild(roboName);
      let roboEmail = document.createElement("p");
      roboEmail.append(document.createTextNode(robot.email));
      divCard.appendChild(roboEmail);
      container.appendChild(divCard);
    });
  }
};

const input = document.getElementsByTagName("input")[0];

const getValue = () => {
  let key = input.value;
  const filter = robots.filter((item) =>
    item.name.toLowerCase().includes(key.toLowerCase())
  );
  displayCards(filter);
};
console.log(input);
displayCards(robots);
input.addEventListener("input", getValue);
