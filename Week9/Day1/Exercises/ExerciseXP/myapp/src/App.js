import logo from "./logo.svg";
import "./App.css";
import Hello from "./Hello";
import UserFavoriteAnimals from "./UserFavoriteAnimals";
import Exercise from "./Exercise3";

const user = {
  firstName: "Bob",
  lastName: "Dylan",
  favAnimals: ["Horse", "Turtle", "Elephant", "Monkey"],
};
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        {/* Exercise 1 */}
        {/* <Hello /> */}

        {/* Exercise 2 */}
        {/* <div>
          <h1>{user.firstName}</h1>
          <h1>{user.lastName}</h1>
          <UserFavoriteAnimals favAnimals={user.favAnimals} />
        </div> */}
        {/* Exercise 3 */}
        <div>
          <Exercise />
        </div>
      </header>
    </div>
  );
}

export default App;
