import { useState } from "react";

const Counter = (props) => {
  let count = 0;
  const addOne = () => {
    count++;
    console.log("count=>", count);
  };
  const [value, setValue] = useState("");
  const handleInput = (e) => {
    setValue(e.target.value);
    // return e.target.value;
  };

  return (
    <>
      <h1>Counter</h1>
      {/* <h2>Count: {count}</h2>
      <button onClick={addOne}>Add</button> */}
      <div>
        <input onChange={handleInput}></input>
        <h4>{value}</h4>
      </div>
    </>
  );
};

export default Counter;
