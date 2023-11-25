import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { addTask } from "../actions/taskActions";

const TaskForm = ({ day }) => {
  const dispatch = useDispatch();
  const [task, setTask] = useState("");

  const handleTaskChange = (e) => {
    setTask(e.target.value);
  };

  const handleAddTask = () => {
    if (task.trim()) {
      dispatch(addTask(day, { id: Date.now(), text: task }));
      setTask("");
    }
  };

  return (
    <div>
      <h4>Add a Task:</h4>
      <input type="text" value={task} onChange={handleTaskChange} />
      <button onClick={handleAddTask}>Add Task</button>
    </div>
  );
};

export default TaskForm;
