import { configureStore, applyMiddleware } from "@reduxjs/toolkit";
import thunk from "redux-thunk"; // Thunk middleware

import counterReducer from "./reducers/counterReducer";

const store = configureStore({
  reducer: {
    counter: counterReducer,
  },
  middleware: [thunk],
});

export default store;
