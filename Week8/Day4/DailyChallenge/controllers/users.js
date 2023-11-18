const Users = require("../models/users");

const getAllUsers = async (req, res) => {
  try {
    const users = await Users.getAllUsers();
    res.json(users);
  } catch (error) {
    console.error(error.message);
    res.status(500).json({ error: "Server Error" });
  }
};

const getUserById = async (req, res) => {
  const { id } = req.params;
  try {
    const user = await Users.getUserById(id);
    if (user) {
      res.json(user);
    } else {
      res.status(404).json({ error: "User not found" });
    }
  } catch (error) {
    console.error(error.message);
    res.status(500).json({ error: "Server Error" });
  }
};

const updateUserById = async (req, res) => {
  const { id } = req.params;
  const userData = req.body;
  try {
    await Users.updateUserById(id, userData);
    res.json({ message: "User updated successfully" });
  } catch (error) {
    console.error(error.message);
    res.status(500).json({ error: "Server Error" });
  }
};

const registerUser = async (req, res) => {
  const { username, email, password, first_name, last_name } = req.body;
  try {
    const existingUser = await Users.getUserByUsername(username);
    if (existingUser) {
      return res.status(400).json({ error: "Username is already taken" });
    }

    await Users.addUser({ username, email, password, first_name, last_name });
    res.json({ message: "Registration successful" });
  } catch (error) {
    console.error(error.message);
    res.status(500).json({ error: "Server Error" });
  }
};

module.exports = { getAllUsers, getUserById, updateUserById, registerUser };
