import { configureStore } from "@reduxjs/toolkit";
import { todoReducer } from "./reducers/reducers";

export default configureStore({
  reducer: {
    todoReducer,
  },
});
