const express = require("express");
const router = express.Router();

const books = [];

router.get("/", (req, res) => {
  res.json(books);
});

router.post("/", (req, res) => {
  // const { title, author } = req.body;
  const newBook = { id: books.length + 1, ...req.body };
  books.push(newBook);
  res.status(201).json(newBook);
});

router.put("/:id", (req, res) => {
  const { id } = req.params;
  const { title, author } = req.body;

  const book = books.find((book) => book.id === parseInt(id));

  if (!book) {
    return res.status(404).json({ error: "Book not found" });
  }

  book.title = title;
  book.author = author;

  res.json(book);
});

router.delete("/:id", (req, res) => {
  const { id } = req.params;

  const bookIndex = books.findIndex((book) => book.id === parseInt(id));

  if (bookIndex === -1) {
    return res.status(404).json({ error: "Book not found" });
  }

  books.splice(bookIndex, 1);

  res.status(204).end();
});

module.exports = router;
