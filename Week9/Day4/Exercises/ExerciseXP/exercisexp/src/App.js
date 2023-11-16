import logo from "./logo.svg";
import "./App.css";
import Car from "./Components/Car";
import Events from "./Components/Events";
import Phone from "./Components/Phone";
import Color from "./Components/Color";

function App() {
  const carInfo = { name: "Ford", model: "Mustang" };

  return (
    <div className="App">
      {/* Exercise 1 */}
      {/* <div>
        <Car name={carInfo.name} model={carInfo.model} />
      </div> */}
      {/* Exercise 2 */}
      {/* <Events /> */}
      {/* Exercise 3 */}
      {/* <Phone /> */}
      {/* Exercise 4 */}
      <Color />
    </div>
  );
}

export default App;
