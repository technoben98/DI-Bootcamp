import React from "react";
import { useDispatch } from "react-redux";
import { toggleTodo, removeTodo } from "./todoSlice";

const TodoItem = ({ todo }) => {
  const dispatch = useDispatch();

  const handleToggleTodo = () => {
    dispatch(toggleTodo(todo.id));
  };

  const handleRemoveTodo = () => {
    dispatch(removeTodo(todo.id));
  };

  return (
    <li>
      <input
        type="checkbox"
        checked={todo.completed}
        onChange={handleToggleTodo}
      />
      <span
        style={{ textDecoration: todo.completed ? "line-through" : "none" }}
      >
        {todo.text}
      </span>
      <button onClick={handleRemoveTodo}>Remove</button>
    </li>
  );
};

export default TodoItem;
