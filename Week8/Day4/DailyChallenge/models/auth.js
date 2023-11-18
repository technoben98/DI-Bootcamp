const db = require("../config/knex");
const bcrypt = require("bcrypt");
const jwt = require("jsonwebtoken");

class Auth {
  static async getUserByUsername(username) {
    return db("hashpwd").where("username", username).first();
  }

  static async addUser(username, password) {
    const hashedPassword = await bcrypt.hash(password, 10);
    return db("hashpwd").insert({
      username,
      password: hashedPassword,
    });
  }

  static generateToken(username) {
    return jwt.sign({ username }, process.env.SECRET_KEY, { expiresIn: "1h" });
  }
}

module.exports = Auth;
