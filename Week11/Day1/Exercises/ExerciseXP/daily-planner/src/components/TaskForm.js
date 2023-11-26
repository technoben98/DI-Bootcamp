import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { addTask, editTask } from "../redux/dayTaskSlice";

const TaskForm = ({ selectedDay, editingTask, onClose }) => {
  const dispatch = useDispatch();
  const [text, setText] = useState(editingTask ? editingTask.text : "");

  const handleSubmit = () => {
    if (editingTask) {
      dispatch(
        editTask({ day: selectedDay, taskId: editingTask.id, newText: text })
      );
    } else {
      dispatch(addTask({ day: selectedDay, task: { id: Date.now(), text } }));
    }
    onClose();
  };

  return (
    <div>
      <h2>{editingTask ? "Edit Task" : "Add Task"}</h2>
      <input
        type="text"
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <button onClick={handleSubmit}>Submit</button>
    </div>
  );
};

export default TaskForm;
