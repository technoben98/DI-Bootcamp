const bcrypt = require("bcrypt");
const fs = require("fs");
const path = require("path");

const usersFilePath = path.join(__dirname, "../data/users.json");

const readUsersFile = () => {
  const usersData = fs.readFileSync(usersFilePath, "utf-8");
  return JSON.parse(usersData);
};

const writeUsersFile = (users) => {
  fs.writeFileSync(usersFilePath, JSON.stringify(users, null, 2), "utf-8");
};

const hashPassword = async (password) => {
  const saltRounds = 10;
  return await bcrypt.hash(password, saltRounds);
};

const registerUser = async (req, res) => {
  try {
    const { name, lastName, email, username, password } = req.body;

    // Check if the username or password already exists
    const existingUsers = readUsersFile();
    const isUsernameTaken = existingUsers.some(
      (user) => user.username === username
    );
    const isEmailTaken = existingUsers.some((user) => user.email === email);

    if (isUsernameTaken || isEmailTaken) {
      return res.status(400).json({ error: "Username or email already taken" });
    }

    const hashedPassword = await hashPassword(password);

    const newUser = {
      id: existingUsers.length + 1,
      name,
      lastName,
      email,
      username,
      password: hashedPassword,
    };

    existingUsers.push(newUser);
    writeUsersFile(existingUsers);

    res.json({ message: "User registered successfully", user: newUser });
  } catch (error) {
    console.error(error.message);
    res.status(500).json({ error: "Server Error" });
  }
};

const loginUser = async (req, res) => {
  try {
    const { username, password } = req.body;

    const existingUsers = readUsersFile();
    const user = existingUsers.find((user) => user.username === username);

    if (!user) {
      return res.status(401).json({ error: "User not found" });
    }

    const isPasswordValid = await bcrypt.compare(password, user.password);

    if (isPasswordValid) {
      res.json({ message: "Login successful", user });
    } else {
      res.status(401).json({ error: "Incorrect password" });
    }
  } catch (error) {
    console.error(error.message);
    res.status(500).json({ error: "Server Error" });
  }
};

const getAllUsers = (req, res) => {
  try {
    const users = readUsersFile();
    res.json(users);
  } catch (error) {
    console.error(error.message);
    res.status(500).json({ error: "Server Error" });
  }
};

const getUserById = (req, res) => {
  try {
    const { id } = req.params;
    const users = readUsersFile();
    const user = users.find((user) => user.id === parseInt(id));

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

const updateUserById = (req, res) => {
  try {
    const { id } = req.params;
    const { name, lastName, email } = req.body;

    const users = readUsersFile();
    const userIndex = users.findIndex((user) => user.id === parseInt(id));

    if (userIndex !== -1) {
      users[userIndex] = {
        ...users[userIndex],
        name: name || users[userIndex].name,
        lastName: lastName || users[userIndex].lastName,
        email: email || users[userIndex].email,
      };

      writeUsersFile(users);
      res.json({
        message: "User updated successfully",
        user: users[userIndex],
      });
    } else {
      res.status(404).json({ error: "User not found" });
    }
  } catch (error) {
    console.error(error.message);
    res.status(500).json({ error: "Server Error" });
  }
};

module.exports = {
  registerUser,
  loginUser,
  getAllUsers,
  getUserById,
  updateUserById,
};
