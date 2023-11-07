const express = require("express");
const router = express.Router();

const todos = [];

router.get("/", (req, res) => {
  res.json(todos);
});

router.post("/", (req, res) => {
  const { title, description } = req.body;
  const newTodo = {
    id: todos.length + 1,
    title,
    description,
  };
  todos.push(newTodo);
  res.status(201).json(newTodo);
});

router.put("/:id", (req, res) => {
  const { id } = req.params;
  const { title, description } = req.body;
  const todo = todos.find((todo) => todo.id === parseInt(id));
  if (!todo) {
    return res.status(404).json({ error: "Todo not found" });
  }
  todo.title = title;
  todo.description = description;
  res.json(todo);
});

router.delete("/:id", (req, res) => {
  const { id } = req.params;
  const todoIndex = todos.findIndex((todo) => todo.id === parseInt(id));
  if (todoIndex === -1) {
    return res.status(404).json({ error: "Todo not found" });
  }
  todos.splice(todoIndex, 1);
  res.status(204).end();
});

module.exports = router;
