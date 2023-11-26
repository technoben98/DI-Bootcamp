import React, { useState } from "react";
import WeatherSearch from "../components/WeatherSearch";
import WeatherDisplay from "../components/WeatherDisplay";

const WeatherPage = () => {
  const [weatherData, setWeatherData] = useState(null);

  const handleWeatherSearch = async (city) => {
    try {
      const data = await fetchWeatherData(city);
      setWeatherData(data);
    } catch (error) {
      console.error("Error fetching weather data:", error);
    }
  };

  const fetchWeatherData = async (city) => {
    const apiKey = process.env.API_KEY;
    const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;

    const response = await fetch(apiUrl);

    if (!response.ok) {
      throw new Error("Weather data not available");
    }

    const weatherJson = await response.json();
    return {
      city: weatherJson.name,
      temperature: `${weatherJson.main.temp}°C`,
      description: weatherJson.weather[0].description,
    };
  };

  return (
    <div>
      <h2>Weather Page</h2>
      <WeatherSearch onSearch={handleWeatherSearch} />
      <WeatherDisplay data={weatherData} />
    </div>
  );
};

export default WeatherPage;
