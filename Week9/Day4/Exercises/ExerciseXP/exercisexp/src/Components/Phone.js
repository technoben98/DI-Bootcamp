import React, { useState } from "react";

const Phone = () => {
  const [brand, setBrand] = useState("Samsung");
  const [model, setModel] = useState("Galaxy S20");
  const [color, setColor] = useState("black");
  const [year, setYear] = useState(2020);

  const changeColor = () => {
    setColor("blue");
  };

  return (
    <div>
      Brand: {brand} <br />
      Model: {model} <br />
      Color: {color} <br />
      Year: {year} <br />
      <button onClick={changeColor}>Change Color</button>
    </div>
  );
};

export default Phone;
