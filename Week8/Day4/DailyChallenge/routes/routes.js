const express = require("express");
const router = express.Router();
const {
  getAllUsers,
  getUserById,
  updateUserById,
  registerUser,
} = require("../controllers/users");
const { loginUser } = require("../controllers/auth");

router.get("/users", getAllUsers);
router.get("/users/:id", getUserById);
router.put("/users/:id", updateUserById);
router.post("/register", registerUser);
router.post("/login", loginUser);

module.exports = router;
