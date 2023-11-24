import React from "react";
import { createContext, useState } from "react";
import ThemeContext from "./Components/ThemeContext";
import "./App.css";

export const AppContext = createContext();

function App() {
  const [style, setStyle] = useState({});
  return (
    <div style={style}>
      <AppContext.Provider value={{ style, setStyle }}>
        <ThemeContext />
      </AppContext.Provider>
    </div>
  );
}
export default App;
