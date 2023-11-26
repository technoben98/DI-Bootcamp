import React from "react";

const WeatherCard = ({ data, onAddToFavorites }) => {
  const { name, main, weather } = data;

  return (
    <div>
      <h3>{name}</h3>
      <p>Temperature: {main.temp}°C</p>
      <p>Weather: {weather[0].description}</p>
      <button onClick={onAddToFavorites}>Add to Favorites</button>
    </div>
  );
};

export default WeatherCard;
