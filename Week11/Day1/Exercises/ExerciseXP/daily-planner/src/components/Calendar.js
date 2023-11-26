import React from "react";

const Calendar = ({ days, onSelectDay }) => {
  return (
    <div>
      <h2>Calendar</h2>
      <ul>
        {days.map((day) => (
          <li
            style={{ cursor: "pointer" }}
            key={day}
            onClick={() => onSelectDay(day)}
          >
            {day}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Calendar;
