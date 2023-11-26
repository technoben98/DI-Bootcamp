import React from "react";
import { Provider } from "react-redux";
import store from "./app/store";
import TodoList from "./features/TodoList";
import AddTodo from "./features/AddTodo";

const App = () => {
  return (
    <Provider store={store}>
      <div>
        <AddTodo />
        <TodoList />
      </div>
    </Provider>
  );
};

export default App;
