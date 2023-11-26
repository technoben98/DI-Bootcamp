import React from "react";
import "./NavBar.css";

const NavBar = ({ currentScore, topScore }) => {
  return (
    <div className="navbar">
      <div>Current Score: {currentScore}</div>
      <div>Top Score: {topScore}</div>
    </div>
  );
};

export default NavBar;
