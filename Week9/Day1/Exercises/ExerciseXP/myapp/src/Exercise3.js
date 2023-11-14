import React, { Component } from "react";
import "./Exercise.css";

const style_header = {
  color: "white",
  backgroundColor: "DodgerBlue",
  padding: "10px",
  fontFamily: "Arial",
};

class Exercise extends Component {
  render() {
    return (
      <div>
        <h1 style={style_header}>Exercise Component</h1>
        <p className="para">This is a paragraph.</p>
        <a href="#">Link</a>
        <form>
          <input type="text" />
          <button type="submit">Submit</button>
        </form>
        <img
          style={{ width: "150px" }}
          src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/React-icon.svg/1200px-React-icon.svg.png"
          alt="Image"
        />
        <ul>
          <li>List Item 1</li>
          <li>List Item 2</li>
          <li>List Item 3</li>
        </ul>
      </div>
    );
  }
}

export default Exercise;
