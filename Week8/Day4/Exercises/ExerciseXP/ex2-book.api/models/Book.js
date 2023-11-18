const db = require("../config/db");

const Book = {
  getAllBooks: async () => {
    try {
      return await db("books").select("*");
    } catch (error) {
      throw error;
    }
  },

  getBookById: async (id) => {
    try {
      const book = await db("books").where("id", id).first();
      return book;
    } catch (error) {
      throw error;
    }
  },
};

module.exports = Book;
