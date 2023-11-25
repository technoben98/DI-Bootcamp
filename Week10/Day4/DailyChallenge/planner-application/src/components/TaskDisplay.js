import React from "react";
import { useSelector } from "react-redux";
import TaskItem from "./TaskItem";

const TaskDisplay = ({ day }) => {
  const tasks = useSelector((state) => state.tasks[day] || []);

  return (
    <div>
      <h4>Tasks:</h4>
      <ul>
        {tasks.map((task) => (
          <TaskItem key={task.id} task={task} day={day} />
        ))}
      </ul>
    </div>
  );
};

export default TaskDisplay;
