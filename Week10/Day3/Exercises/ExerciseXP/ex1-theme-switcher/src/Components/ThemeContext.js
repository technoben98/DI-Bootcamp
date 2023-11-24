import { useContext } from "react";
import { AppContext } from "../App.js";
import "../App.css";

const ThemeContext = (props) => {
  const { style, setStyle } = useContext(AppContext);

  const dark = {
    backgroundColor: "black",
    color: "white",
  };
  const light = {
    backgroundColor: "white",
    color: "black",
  };

  const changeStyle = () => {
    if (style.backgroundColor == dark.backgroundColor) {
      setStyle(light);
    } else {
      setStyle(dark);
    }
  };

  return (
    <div style={{ width: "50%", height: "100vh" }}>
      <h1>Change theme:</h1>
      <label class="switch">
        <button type="button" onClick={changeStyle}>
          Theme
        </button>
        <span class="slider round"></span>
      </label>
    </div>
  );
};

export default ThemeContext;
