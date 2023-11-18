const db = require("../config/db");

class Post {
  static async getAllPosts() {
    try {
      const posts = await db.select("*").from("posts");
      return posts;
    } catch (error) {
      throw error;
    }
  }

  static async getPostById(id) {
    try {
      const post = await db.select("*").from("posts").where("id", id).first();
      return post;
    } catch (error) {
      throw error;
    }
  }

  static async createPost(title, content) {
    try {
      const [newPost] = await db("posts")
        .insert({ title, content })
        .returning("*");
      return newPost;
    } catch (error) {
      throw error;
    }
  }

  static async updatePost(id, title, content) {
    try {
      const [updatedPost] = await db("posts")
        .where("id", id)
        .update({ title, content })
        .returning("*");
      return updatedPost;
    } catch (error) {
      throw error;
    }
  }

  static async deletePost(id) {
    try {
      await db("posts").where("id", id).del();
    } catch (error) {
      throw error;
    }
  }
}

module.exports = Post;
