import { createAction } from "@reduxjs/toolkit";

export const addTask = createAction("dayTasks/addTask");
export const editTask = createAction("dayTasks/editTask");
export const deleteTask = createAction("dayTasks/deleteTask");
