import React from "react";
import { useSelector } from "react-redux";

const TaskList = ({ selectedDay }) => {
  const tasks = useSelector((state) => state.dayTasks[selectedDay] || []);

  return (
    <div>
      <h2>Tasks for {selectedDay}</h2>
      <ul>
        {tasks.map((task) => (
          <li key={task.id}>{task.text}</li>
        ))}
      </ul>
    </div>
  );
};

export default TaskList;
