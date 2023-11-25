import { createAction } from "@reduxjs/toolkit";

export const addTask = createAction("tasks/add", (day, task) => ({
  payload: { day, task },
}));

export const editTask = createAction(
  "tasks/edit",
  (day, taskId, updatedTask) => ({
    payload: { day, taskId, updatedTask },
  })
);

export const deleteTask = createAction("tasks/delete", (day, taskId) => ({
  payload: { day, taskId },
}));
