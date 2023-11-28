import "./App.css";
import React from "react";
import { Provider } from "react-redux";
import store from "./app/store";
import UsersList from "./features/users/UsersList";

const App = () => {
  return (
    <Provider store={store}>
      <div>
        <h1>Redux Thunk Users List App</h1>
        <UsersList />
      </div>
    </Provider>
  );
};

export default App;
