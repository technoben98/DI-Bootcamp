import { Provider } from "react-redux";
import "./App.css";
import Counter from "./components/Counter";
import store from "./redux/store";

function App() {
  return (
    <div className="App">
      <Provider store={store}>
        <Counter />
      </Provider>
    </div>
  );
}

export default App;
