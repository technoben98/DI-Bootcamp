import React, { Component } from "react";

class Color extends Component {
  constructor(props) {
    super(props);
    this.state = {
      favoriteColor: "red",
    };
  }

  shouldComponentUpdate(nextProps, nextState) {
    // Part 1
    return true;
  }

  componentDidMount() {
    // Part 2
    setTimeout(() => {
      this.setState({ favoriteColor: "yellow" });
    }, 1000);
  }

  componentDidUpdate(prevProps, prevState) {
    // Part 2
    console.log("after update");
  }

  getSnapshotBeforeUpdate(prevProps, prevState) {
    // Part 3
    console.log("in getSnapshotBeforeUpdate");
    return null;
  }

  changeColor = () => {
    this.setState({ favoriteColor: "blue" });
  };

  render() {
    console.log("Rendering...");
    return (
      <div>
        <h1>
          My Favorite Color is <i>{this.state.favoriteColor}</i>
        </h1>
        <button onClick={this.changeColor}>Change Color</button>
      </div>
    );
  }
}

export default Color;
