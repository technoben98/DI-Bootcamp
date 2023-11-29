import { createReducer } from "@reduxjs/toolkit";
import { ageUpAsync, ageDownAsync } from "../actions/counterActions";

const initialState = {
  age: 20,
  loading: false,
};

const counterReducer = createReducer(initialState, (builder) => {
  builder
    .addCase(ageUpAsync.pending, (state) => {
      state.loading = true;
    })
    .addCase(ageUpAsync.fulfilled, (state, action) => {
      state.age = action.payload;
      state.loading = false;
    })
    .addCase(ageDownAsync.pending, (state) => {
      state.loading = true;
    })
    .addCase(ageDownAsync.fulfilled, (state, action) => {
      state.age = action.payload;
      state.loading = false;
    });
});

export default counterReducer;
