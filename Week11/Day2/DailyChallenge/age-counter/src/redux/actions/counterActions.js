import { createAsyncThunk } from "@reduxjs/toolkit";

export const ageUpAsync = createAsyncThunk(
  "counter/ageUpAsync",
  async (delay, thunkAPI) => {
    await new Promise((resolve) => setTimeout(resolve, delay));
    return thunkAPI.getState().counter.age + 1;
  }
);

export const ageDownAsync = createAsyncThunk(
  "counter/ageDownAsync",
  async (delay, thunkAPI) => {
    await new Promise((resolve) => setTimeout(resolve, delay));
    return thunkAPI.getState().counter.age - 1;
  }
);
