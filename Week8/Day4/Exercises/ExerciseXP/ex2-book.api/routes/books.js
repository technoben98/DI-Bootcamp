const express = require("express");
const router = express.Router();
const { getAllBooks, getBookById } = require("../controllers/books");

router.get("/", getAllBooks);
router.get("/:bookId", getBookById);

module.exports = router;
