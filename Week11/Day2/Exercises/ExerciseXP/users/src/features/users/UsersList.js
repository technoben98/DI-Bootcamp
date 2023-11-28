import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { fetchUsersData } from "./userActions";

const UsersList = () => {
  const dispatch = useDispatch();
  const usersData = useSelector((state) => state.user.data);
  const error = useSelector((state) => state.user.error);

  useEffect(() => {
    dispatch(fetchUsersData());
  }, [dispatch]);

  return (
    <div>
      {error ? (
        <p>Error: {error}</p>
      ) : (
        <div className="container">
          {usersData.map((user) => (
            <div className="card" key={user.id}>
              <h1>{user.name}</h1>
              <p>Email: {user.email}</p>
              <p>City: {user.address.city}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default UsersList;
