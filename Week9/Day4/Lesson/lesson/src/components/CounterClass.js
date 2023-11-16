import React from "react";

class CounterClass extends React.Component {
  constructor() {
    super();
    this.state = {
      count: 0,
      inputValue: "",
    };
  }

  handleInput = (e) => {
    this.setState({ inputValue: e.targer.value });
  };

  render() {
    console.log("2 render");
    return (
      <>
        <h1>Counter Class</h1>
        {/* <h2>Count: {this.state.count}</h2> */}
        {/* <button onClick={addOne}>Add</button> */}
        <div>
          <input onChange={this.handleChange}></input>
          <h4>{this.state.inputValue}</h4>
        </div>
      </>
    );
  }
}
