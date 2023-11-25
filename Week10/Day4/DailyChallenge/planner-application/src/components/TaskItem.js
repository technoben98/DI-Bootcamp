import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { editTask, deleteTask } from "../actions/taskActions";

const TaskItem = ({ task, day }) => {
  const dispatch = useDispatch();
  const [isEditing, setIsEditing] = useState(false);
  const [editedTask, setEditedTask] = useState(task.text);

  const handleTaskChange = (e) => {
    setEditedTask(e.target.value);
  };

  const handleEditTask = () => {
    dispatch(editTask(day, task.id, { ...task, text: editedTask }));
    setIsEditing(false);
  };

  const handleDeleteTask = () => {
    dispatch(deleteTask(day, task.id));
  };

  return (
    <li>
      {isEditing ? (
        <div>
          <input type="text" value={editedTask} onChange={handleTaskChange} />
          <button onClick={handleEditTask}>Save</button>
        </div>
      ) : (
        <div>
          {task.text}
          <button onClick={() => setIsEditing(true)}>Edit</button>
          <button onClick={handleDeleteTask}>Delete</button>
        </div>
      )}
    </li>
  );
};

export default TaskItem;
