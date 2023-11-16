import React, { useState } from "react";

const Vote = () => {
  const [languages, setLanguages] = useState([
    { name: "Php", votes: 0 },
    { name: "Python", votes: 0 },
    { name: "JavaScript", votes: 0 },
    { name: "Java", votes: 0 },
  ]);

  const incrementVote = (index) => {
    const updatedLanguages = [...languages];
    updatedLanguages[index].votes++;
    setLanguages(updatedLanguages);
  };

  return (
    <div>
      <h1>Languages Votes</h1>
      {languages.map((language, index) => (
        <div key={index}>
          <p>
            {language.name} - {language.votes}
          </p>
          <button onClick={() => incrementVote(index)}>Vote</button>
        </div>
      ))}
    </div>
  );
};

export default Vote;
