import { fetchUsersSuccess, fetchUsersFailure } from "./userSlice";

export const fetchUsersData = () => async (dispatch) => {
  try {
    const response = await fetch("https://jsonplaceholder.typicode.com/users");
    const usersData = await response.json();
    dispatch(fetchUsersSuccess(usersData));
  } catch (error) {
    dispatch(fetchUsersFailure("Failed to fetch users data"));
  }
};
