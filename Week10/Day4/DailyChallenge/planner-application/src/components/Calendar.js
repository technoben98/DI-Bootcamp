import React, { useState } from "react";
import { useDispatch } from "react-redux";
import TaskDisplay from "./TaskDisplay";
import TaskForm from "./TaskForm";

const Calendar = () => {
  const [selectedDay, setSelectedDay] = useState(null);
  const dispatch = useDispatch();

  const handleDayClick = (day) => {
    setSelectedDay(day);
  };

  return (
    <div>
      <h2>Calendar</h2>
      <div>
        {[1, 2, 3, 4, 5].map((day) => (
          <button key={day} onClick={() => handleDayClick(day)}>
            Day {day}
          </button>
        ))}
      </div>
      {selectedDay && (
        <div>
          <h3>Tasks for Day {selectedDay}</h3>
          <TaskDisplay day={selectedDay} />
          <TaskForm day={selectedDay} />
        </div>
      )}
    </div>
  );
};

export default Calendar;
