import { createReducer } from "@reduxjs/toolkit";
import { addTask, editTask, deleteTask } from "../actions/taskActions";

const initialState = {};

const taskReducer = createReducer(initialState, (builder) => {
  builder
    .addCase(addTask, (state, action) => {
      const { day, task } = action.payload;
      state[day] = [...(state[day] || []), task];
    })
    .addCase(editTask, (state, action) => {
      const { day, taskId, updatedTask } = action.payload;
      state[day] = state[day].map((t) => (t.id === taskId ? updatedTask : t));
    })
    .addCase(deleteTask, (state, action) => {
      const { day, taskId } = action.payload;
      state[day] = state[day].filter((t) => t.id !== taskId);
    });
});

export default taskReducer;
