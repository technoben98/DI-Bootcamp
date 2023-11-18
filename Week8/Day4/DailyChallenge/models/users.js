const db = require("../config/knex");
const bcrypt = require("bcrypt");

class Users {
  static async getAllUsers() {
    return db("users").select(
      "id",
      "email",
      "username",
      "first_name",
      "last_name"
    );
  }

  static async getUserById(id) {
    return db("users")
      .select("id", "email", "username", "first_name", "last_name")
      .where("id", id)
      .first();
  }

  static async updateUserById(id, userData) {
    return db("users").where("id", id).update(userData);
  }

  static async addUser(user) {
    const { username, email, password, first_name, last_name } = user;
    const hashedPassword = await bcrypt.hash(password, 10);

    return db.transaction(async (trx) => {
      const [userId] = await trx("users")
        .insert({
          email,
          username,
          first_name,
          last_name,
        })
        .returning("id");

      await trx("hashpwd").insert({
        user_id: userId,
        username,
        password: hashedPassword,
      });
    });
  }

  static async getUserByUsername(username) {
    return db("hashpwd").where("username", username).first();
  }
}

module.exports = Users;
