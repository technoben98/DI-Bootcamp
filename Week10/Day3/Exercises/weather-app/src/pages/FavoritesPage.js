import React from "react";
import { useSelector } from "react-redux";

const FavoritesPage = () => {
  // Retrieve favorite cities from the Redux store
  const favorites = useSelector((state) => state.favorites);

  return (
    <div>
      <h2>Favorites Page</h2>
      <ul>
        {favorites.map((fav, index) => (
          <li key={index}>{fav}</li>
        ))}
      </ul>
    </div>
  );
};

export default FavoritesPage;
