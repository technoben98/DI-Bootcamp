const express = require("express");
const app = express();

// Simulated database
const data = [
  { id: 1, title: "First Blog Post", content: "This is the first blog post." },
  {
    id: 2,
    title: "Second Blog Post",
    content: "This is the second blog post.",
  },
];

app.get("/posts", (req, res) => {
  res.json(data);
});

app.get("/posts/:id", (req, res) => {
  const id = parseInt(req.params.id);
  const post = data.find((post) => post.id === id);

  if (!post) {
    res.sendStatus(404);
  } else {
    res.json(post);
  }
});

app.post("/posts", (req, res) => {
  const newPost = { id: data.length + 1, ...req.body };
  data.push(newPost);

  res.sendStatus(201).json(data);
});

app.put("/posts/:id", (req, res) => {
  let { id } = req.params;
  const post = data.find((item) => item.id == id);
  if (!post) return res.status(404).json({ message: "Post Not Found" });
  let { title, content } = { ...req.body };
  post.title = title;
  post.content = content;
  res.status(201).json(data);
});

app.delete("/posts/:id", (req, res) => {
  const { id } = req.params;
  const indx = data.findIndex((item) => item.id == id);
  if (indx === -1) return res.status(404).json({ message: "Post not found" });
  data.splice(indx, 1);
  res.json(data);
});

const port = 3000;
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
