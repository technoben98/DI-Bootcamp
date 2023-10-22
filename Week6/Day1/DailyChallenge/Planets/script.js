const planets = [
    { name: "Mercury", color: "#d9d9d9", moons: 0 },
    { name: "Venus", color: "#ffcc66", moons: 0 },
    { name: "Earth", color: "#0066ff", moons: 1 },
    { name: "Mars", color: "#ff6666", moons: 2 },
    { name: "Jupiter", color: "#ffaa33", moons: 79 },
    { name: "Saturn", color: "#ffcc99", moons: 82 },
    { name: "Uranus", color: "#66ccff", moons: 27 },
    { name: "Neptune", color: "#003366", moons: 14 }
];
  
const listPlanets = document.querySelector(".listPlanets");


for (let i = 0; i < planets.length; i++) {
    const planet = planets[i];

    const planetDiv = document.createElement("div");
    planetDiv.className = "planet";
    planetDiv.style.backgroundColor = planet.color;
    planetDiv.textContent = planet.name;

    for (let j = 0; j < planet.moons; j++) {
        const moonDiv = document.createElement("div");
        moonDiv.className = "moon";
        planetDiv.appendChild(moonDiv);
    }

    listPlanets.appendChild(planetDiv);
}