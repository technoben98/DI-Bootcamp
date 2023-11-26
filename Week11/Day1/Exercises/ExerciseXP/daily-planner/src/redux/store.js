import { configureStore } from "@reduxjs/toolkit";
import dayTasksReducer from "./dayTaskSlice";

const store = configureStore({
  reducer: {
    dayTasks: dayTasksReducer,
  },
});

export default store;
