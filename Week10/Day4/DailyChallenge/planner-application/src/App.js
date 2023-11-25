import React from "react";
import { Provider } from "react-redux";
import Calendar from "./components/Calendar";
import store from "./store/configureStore";

const App = () => {
  return (
    <Provider store={store}>
      <div>
        <h1>Daily Planner App</h1>
        <Calendar />
      </div>
    </Provider>
  );
};

export default App;
