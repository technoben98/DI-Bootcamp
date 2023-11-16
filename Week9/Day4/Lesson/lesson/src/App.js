import logo from "./logo.svg";
import "./App.css";
import Counter from "../src/components/Counter";
import Users from "../src/components/Users";
import UsersFunction from "./components/UsersFunction";
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <UsersFunction />
      </header>
    </div>
  );
}

export default App;
