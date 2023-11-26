import React, { useState, useEffect } from "react";
import NavBar from "./components/NavBar";
import Card from "./components/Card";
import "./App.css";
import superheroesData from "./superheroes.json";

const App = () => {
  const [superheroes, setSuperheroes] = useState([]);
  const [selectedSuperheroes, setSelectedSuperheroes] = useState([]);
  const [currentScore, setCurrentScore] = useState(0);
  const [topScore, setTopScore] = useState(0);

  useEffect(() => {
    console.log("Superheroes data:", superheroesData);
    const superheroesArray = superheroesData.superheroes;
    setSuperheroes(superheroesArray);
  }, []);

  const shuffleCards = () => {
    setSuperheroes((prevSuperheroes) =>
      [...prevSuperheroes].sort(() => Math.random() - 0.5)
    );
  };

  const handleClick = (id) => {
    console.log("Clicked superhero ID:", id);
    console.log("Selected superheroes:", selectedSuperheroes);
    if (selectedSuperheroes.includes(id)) {
      setCurrentScore(0);
      setSelectedSuperheroes([]);
    } else {
      setCurrentScore(currentScore + 1);
      setSelectedSuperheroes([...selectedSuperheroes, id]);
    }
    shuffleCards();
  };

  useEffect(() => {
    if (currentScore > topScore) {
      setTopScore(currentScore);
    }
  }, [currentScore, topScore]);

  return (
    <div className="app">
      <NavBar currentScore={currentScore} topScore={topScore} />
      <div className="card-container">
        {superheroes.map((superhero) => (
          <Card
            key={superhero.id}
            superhero={superhero}
            handleClick={handleClick}
          />
        ))}
      </div>
    </div>
  );
};

export default App;
