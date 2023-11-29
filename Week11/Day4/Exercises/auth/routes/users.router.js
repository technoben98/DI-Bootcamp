import express from "express";
import {
  _login,
  _register,
  _refreshToken,
} from "../controllers/users.controller.js";
import { verifytoken } from "../middlawares/verifytoken.js";

const u_router = express.Router();

u_router.post("/register", _register);

u_router.post("/login", _login);

u_router.get("/verify", verifytoken, (req, res) => {
  res.sendStatus(201);
});

u_router.get("/logout", (req, res) => {
  res.clearCookie("token");
  res.json({ message: "Logout successful" });
});

u_router.post("/refresh", _refreshToken);

export default u_router;
