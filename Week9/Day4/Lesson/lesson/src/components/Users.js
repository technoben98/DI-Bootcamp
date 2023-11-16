import React from "react";

class Users extends React.Component {
  constructor() {
    super();
    this.state = {
      users: [],
    };
  }
  getAllUsers = async () => {
    try {
      const res = await fetch("https://jsonplaceholder.typicode.com/users");
      const data = await res.json();
      console.log(data);
      this.setState({ users: data });
    } catch (error) {
      console.log(error);
    }
  };
  render() {
    return (
      <>
        <div>
          <button onClick={this.getAllUsers}>Get Users</button>
        </div>

        {this.state.users.map((item) => {
          return (
            <div>
              <h4>
                {item.name}, {item.email}
              </h4>
            </div>
          );
        })}
      </>
    );
  }
}

export default Users;
