import { login, register } from "../models/users.model.js";
import bcrypt from "bcrypt";
import jwt from "jsonwebtoken";
import dotenv from "dotenv";
dotenv.config();

export const _login = async (req, res) => {
  try {
    const { email, password } = req.body;

    const row = await login(email.toLowerCase());

    if (row.length === 0)
      return res.status(404).json({ msg: "email not exist" });

    const match = bcrypt.compareSync(password + "", row[0].password);
    if (!match) return res.status(404).json({ msg: "wrong password" });

    const userid = row[0].id;
    const useremail = row[0].email;

    const secret = process.env.ACCESS_TOKEN_SECRET;

    const accesstoken = jwt.sign({ userid, useremail }, secret, {
      expiresIn: "60s",
    });

    res.cookie("token", accesstoken, {
      httpOnly: true,
      maxAge: 60 * 1000,
    });

    // Implementing of refresh logic
    const refreshSecret = process.env.REFRESH_TOKEN_SECRET;
    const refreshToken = jwt.sign({ userid, useremail }, refreshSecret, {
      expiresIn: "60s",
    });

    res.cookie("refreshToken", refreshToken, {
      httpOnly: true,
      maxAge: 60 * 1000,
    });

    res.json({ accesstoken, refreshToken });
  } catch (e) {
    console.log("_login=>", e);
    res.status(404).json({ msg: "something went wrong" });
  }
};

export const _register = async (req, res) => {
  const { email, password } = req.body;
  const loweremail = email.toLowerCase();
  const salt = bcrypt.genSaltSync(10);
  const hash = bcrypt.hashSync(password + "", salt);
  try {
    const row = await register(loweremail, hash);
    res.json(row);
  } catch (e) {
    console.log("_register=>", e);
    res.status(404).json({ msg: "email allready exist" });
  }
};

export const _refreshToken = async (req, res) => {
  try {
    const refreshToken = req.cookies.refreshToken;

    if (!refreshToken) return res.status(401).json({ msg: "Unauthorized" });

    jwt.verify(
      refreshToken,
      process.env.REFRESH_TOKEN_SECRET,
      (err, decoded) => {
        if (err) return res.status(403).json({ msg: err.message });

        const newAccessToken = jwt.sign(
          { userid: decoded.userid, useremail: decoded.useremail },
          process.env.ACCESS_TOKEN_SECRET,
          {
            expiresIn: "60s",
          }
        );

        res.cookie("token", newAccessToken, {
          httpOnly: true,
          maxAge: 60 * 1000,
        });

        res.json({ newAccessToken });
      }
    );
  } catch (e) {
    console.log("_refresh=>", e);
    res.status(404).json({ msg: "Not refreshed" });
  }
};
