import React, { useState } from "react";
import Garage from "./Garage";

const Car = (props) => {
  const [color, setColor] = useState("red");

  return (
    <div>
      <Garage size="small" />
      <h1>
        This {props.name} {props.model} is {color}
      </h1>
    </div>
  );
};

export default Car;
