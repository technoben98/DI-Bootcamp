import { createSlice } from "@reduxjs/toolkit";

const userSlice = createSlice({
  name: "user",
  initialState: { data: [], error: null },
  reducers: {
    fetchUsersSuccess: (state, action) => {
      state.data = action.payload;
      state.error = null;
    },
    fetchUsersFailure: (state, action) => {
      state.error = action.payload;
    },
  },
});

export const { fetchUsersSuccess, fetchUsersFailure } = userSlice.actions;
export default userSlice.reducer;
