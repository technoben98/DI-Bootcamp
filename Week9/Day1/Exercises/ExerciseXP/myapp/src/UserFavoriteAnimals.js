import React, { Component } from "react";

class UserFavoriteAnimals extends Component {
  render() {
    const { favAnimals } = this.props;

    return (
      <div>
        {favAnimals.map((animal, index) => (
          <div key={index}>{animal}</div>
        ))}
      </div>
    );
  }
}

export default UserFavoriteAnimals;
