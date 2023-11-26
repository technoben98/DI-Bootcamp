import React, { useState } from "react";
import { Provider } from "react-redux";
import Calendar from "./components/Calendar";
import TaskList from "./components/TaskList";
import TaskForm from "./components/TaskForm";
import store from "./redux/store";

const App = () => {
  const [selectedDay, setSelectedDay] = useState(null);
  const [editingTask, setEditingTask] = useState(null);

  const handleSelectDay = (day) => {
    setSelectedDay(day);
    setEditingTask(null);
  };

  const handleEditTask = (task) => {
    setEditingTask(task);
  };

  const handleCloseForm = () => {
    setEditingTask(null);
  };

  return (
    <Provider store={store}>
      <div>
        <Calendar
          days={["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]}
          onSelectDay={handleSelectDay}
        />
        {selectedDay && <TaskList selectedDay={selectedDay} />}
        <TaskForm
          selectedDay={selectedDay}
          editingTask={editingTask}
          onClose={handleCloseForm}
        />
      </div>
    </Provider>
  );
};

export default App;
