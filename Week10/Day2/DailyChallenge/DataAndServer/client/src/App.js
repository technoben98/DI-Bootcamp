import React, { useState, useEffect } from "react";
import "./App.css";
// Part 1
// function App() {
//   const [message, setMessage] = useState("");

//   useEffect(() => {
//     const fetchData = async () => {
//       try {
//         const response = await fetch("http://localhost:5000/api/hello");
//         const data = await response.json();
//         setMessage(data.message);
//       } catch (error) {
//         console.error("Error fetching data:", error);
//       }
//     };

//     fetchData();
//   }, []);

//   return (
//     <div className="App">
//       <header className="App-header">
//         <h1>{message}</h1>
//       </header>
//     </div>
//   );
// }
// Part 2
const App = () => {
  const [inputValue, setInputValue] = useState("");
  const [responseMessage, setResponseMessage] = useState("");

  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      const response = await fetch("http://localhost:5000/api/world", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ value: inputValue }),
      });

      const data = await response.json();
      setResponseMessage(data.message);
    } catch (error) {
      console.error("Error sending POST request:", error);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>{responseMessage}</h1>
        <form onSubmit={handleSubmit}>
          <label>
            Enter something:
            <input
              type="text"
              value={inputValue}
              onChange={handleInputChange}
            />
          </label>
          <button type="submit">Submit</button>
        </form>
      </header>
    </div>
  );
};
export default App;
