const Book = require("../models/Book");

const getAllBooks = async (req, res) => {
  try {
    const books = await Book.getAllBooks();
    res.json(books);
  } catch (error) {
    console.error(error.message);
    res.status(500).json({ error: "Server Error" });
  }
};

const getBookById = async (req, res) => {
  const { bookId } = req.params;
  try {
    const book = await Book.getBookById(bookId);
    if (book) {
      res.json(book);
    } else {
      res.status(404).json({ error: "Book not found" });
    }
  } catch (error) {
    console.error(error.message);
    res.status(500).json({ error: "Server Error" });
  }
};

module.exports = { getAllBooks, getBookById };
