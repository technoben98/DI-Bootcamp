import React, { useReducer, useState, useRef } from "react";

// Reducer function
function todoReducer(state, action) {
  switch (action.type) {
    case "ADD_TODO":
      return [
        ...state,
        { id: Date.now(), text: action.text, completed: false },
      ];
    case "REMOVE_TODO":
      return state.filter((todo) => todo.id !== action.id);
    case "TOGGLE_TODO":
      return state.map((todo) =>
        todo.id === action.id ? { ...todo, completed: !todo.completed } : todo
      );
    case "EDIT_TODO":
      return state.map((todo) =>
        todo.id === action.id ? { ...todo, text: action.text } : todo
      );
    case "FILTER_TASKS":
      return state;
    default:
      return state;
  }
}

function TodoList() {
  const [todos, dispatch] = useReducer(todoReducer, []);
  const [todoText, setTodoText] = useState("");
  const [editedText, setEditedText] = useState("");
  const [filter, setFilter] = useState("all");
  const inputRef = useRef(null);
  const editedTaskRef = useRef(null);

  const handleAddTodo = () => {
    if (todoText.trim() === "") return;
    dispatch({ type: "ADD_TODO", text: todoText });
    setTodoText("");
  };

  const handleRemoveTodo = (id) => {
    dispatch({ type: "REMOVE_TODO", id });
  };

  const handleToggleTodo = (id) => {
    dispatch({ type: "TOGGLE_TODO", id });
  };

  const handleEditTodo = (id) => {
    const editedTask = todos.find((todo) => todo.id === id);
    setEditedText(editedTask.text);
    editedTaskRef.current = id;
    if (inputRef.current) {
      inputRef.current.focus();
    }
  };

  const handleSaveEdit = () => {
    dispatch({
      type: "EDIT_TODO",
      id: editedTaskRef.current,
      text: editedText,
    });
    setEditedText("");
    editedTaskRef.current = null;
  };

  const handleFilterTasks = (filterType) => {
    setFilter(filterType);
  };

  const filteredTodos =
    filter === "all"
      ? todos
      : filter === "completed"
      ? todos.filter((todo) => todo.completed)
      : todos.filter((todo) => !todo.completed);

  return (
    <div>
      <h1>Task Manager</h1>
      <div>
        <input
          type="text"
          placeholder="Add a new task"
          value={todoText}
          onChange={(e) => setTodoText(e.target.value)}
        />
        <button onClick={handleAddTodo}>Add Task</button>
      </div>
      <div>
        <label>Filter Tasks: </label>
        <button onClick={() => handleFilterTasks("all")}>All</button>
        <button onClick={() => handleFilterTasks("completed")}>
          Completed
        </button>
        <button onClick={() => handleFilterTasks("active")}>Active</button>
      </div>
      <ul>
        {filteredTodos.map((todo) => (
          <li key={todo.id}>
            <input
              type="checkbox"
              checked={todo.completed}
              onChange={() => handleToggleTodo(todo.id)}
            />
            {editedTaskRef.current === todo.id ? (
              <>
                <input
                  ref={inputRef}
                  type="text"
                  value={editedText}
                  onChange={(e) => setEditedText(e.target.value)}
                />
                <button onClick={handleSaveEdit}>Save</button>
              </>
            ) : (
              <>
                <span>{todo.text}</span>
                <button onClick={() => handleEditTodo(todo.id)}>Edit</button>
                <button onClick={() => handleRemoveTodo(todo.id)}>
                  Remove
                </button>
              </>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default TodoList;
