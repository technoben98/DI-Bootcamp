import { createSlice } from "@reduxjs/toolkit";

const dayTasksSlice = createSlice({
  name: "dayTasks",
  initialState: {},
  reducers: {
    addTask: (state, action) => {
      const { day, task } = action.payload;
      if (!state[day]) {
        state[day] = [];
      }
      state[day].push(task);
    },
    editTask: (state, action) => {
      const { day, taskId, newText } = action.payload;
      const taskIndex = state[day].findIndex((task) => task.id === taskId);
      if (taskIndex !== -1) {
        state[day][taskIndex].text = newText;
      }
    },
    deleteTask: (state, action) => {
      const { day, taskId } = action.payload;
      state[day] = state[day].filter((task) => task.id !== taskId);
    },
  },
});

export const { addTask, editTask, deleteTask } = dayTasksSlice.actions;
export default dayTasksSlice.reducer;
