import React, { Component } from "react";

class Child extends Component {
  componentWillUnmount() {
    alert("Child component will unmount");
  }

  render() {
    return <h2>Hello World!</h2>;
  }
}

class Parent extends Component {
  constructor(props) {
    super(props);
    this.state = {
      show: true,
    };
  }

  componentWillUnmount() {
    console.log("App component will unmount");
  }

  handleDelete = () => {
    this.setState({ show: false });
  };

  render() {
    return (
      <div>
        {this.state.show && <Child />}
        <button onClick={this.handleDelete}>Delete</button>
      </div>
    );
  }
}

export default Parent;
