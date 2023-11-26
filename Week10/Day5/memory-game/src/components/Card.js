import React from "react";
import "./Card.css";

const Card = ({ superhero, handleClick }) => {
  return (
    <div className="card" onClick={() => handleClick(superhero.id)}>
      <img src={superhero.image} alt={superhero.name} />
      <div className="card-info">
        <p>{superhero.name}</p>
        <p>{superhero.occupation}</p>
      </div>
    </div>
  );
};

export default Card;
