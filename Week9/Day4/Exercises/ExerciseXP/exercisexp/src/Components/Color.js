import React, { useState, useEffect } from "react";

const Color = () => {
  const [favoriteColor, setFavoriteColor] = useState("red");

  useEffect(() => {
    alert("useEffect reached");
  }, []);

  const changeColor = () => {
    setFavoriteColor("blue");
  };

  return (
    <div>
      <h1>
        My Favorite Color is <it>{favoriteColor}</it>
      </h1>
      <button onClick={changeColor}>Change Color</button>
    </div>
  );
};

export default Color;
