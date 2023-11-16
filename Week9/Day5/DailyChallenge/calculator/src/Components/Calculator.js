import React, { useState } from "react";

const Calculator = () => {
  const [num1, setNum1] = useState(0);
  const [num2, setNum2] = useState(0);
  const [operation, setOperation] = useState("addition");
  const [result, setResult] = useState(0);

  const handleNum1Change = (e) => {
    setNum1(Number(e.target.value));
  };

  const handleNum2Change = (e) => {
    setNum2(Number(e.target.value));
  };

  const handleOperationChange = (e) => {
    setOperation(e.target.value);
  };

  const calculateResult = () => {
    let calculatedResult;

    switch (operation) {
      case "addition":
        calculatedResult = num1 + num2;
        break;
      case "subtraction":
        calculatedResult = num1 - num2;
        break;
      case "multiplication":
        calculatedResult = num1 * num2;
        break;
      case "division":
        calculatedResult = num1 / num2;
        break;
      default:
        calculatedResult = 0;
    }

    setResult(calculatedResult);
  };

  return (
    <div style={{ backgroundColor: "darkviolet", height: "100vh" }}>
      <div style={{ display: "flex", padding: "20px" }}>
        <div style={{ padding: "30px" }}>
          <input
            style={{
              height: "50px",
              borderRadius: "5px",
              border: "none",
              fontSize: "1.5em",
            }}
            type="number"
            value={num1}
            onChange={handleNum1Change}
          />
        </div>
        <div style={{ padding: "30px" }}>
          <input
            style={{
              height: "50px",
              borderRadius: "5px",
              border: "none",
              fontSize: "1.5em",
            }}
            type="number"
            value={num2}
            onChange={handleNum2Change}
          />
        </div>
      </div>

      {/* <label>Operation:</label> */}
      <select
        style={{
          height: "50px",
          borderRadius: "5px",
          border: "none",
          marginLeft: "300px",
          fontSize: "1.5em",
        }}
        value={operation}
        onChange={handleOperationChange}
      >
        <option value="addition">Addition</option>
        <option value="subtraction">Subtraction</option>
        <option value="multiplication">Multiplication</option>
        <option value="division">Division</option>
      </select>
      <br />
      <button
        style={{
          height: "50px",
          borderRadius: "5px",
          border: "none",
          marginTop: "50px",
          marginLeft: "310px",
          fontSize: "1.5em",
        }}
        onClick={calculateResult}
      >
        Calculate
      </button>
      <br />
      <p style={{ display: "block", marginLeft: "350px", fontSize: "3em" }}>
        {result}
      </p>
    </div>
  );
};

export default Calculator;
