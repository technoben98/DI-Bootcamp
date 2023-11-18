const Post = require("../models/post.js");

const getPosts = async (req, res) => {
  try {
    const posts = await Post.getAllPosts();
    res.json(posts);
  } catch (error) {
    console.error(error.message);
    res.status(500).json({ error: "Server Error" });
  }
};

const getPostById = async (req, res) => {
  const { id } = req.params;
  try {
    const post = await Post.getPostById(id);
    res.json(post);
  } catch (error) {
    console.error(error.message);
    res.status(500).json({ error: "Server Error" });
  }
};

const createPost = async (req, res) => {
  const { title, content } = req.body;
  try {
    const newPost = await Post.createPost(title, content);
    res.json(newPost);
  } catch (error) {
    console.error(error.message);
    res.status(500).json({ error: "Server Error" });
  }
};

const updatePost = async (req, res) => {
  const { id } = req.params;
  const { title, content } = req.body;
  try {
    const updatedPost = await Post.updatePost(id, title, content);
    res.json(updatedPost);
  } catch (error) {
    console.error(error.message);
    res.status(500).json({ error: "Server Error" });
  }
};

const deletePost = async (req, res) => {
  const { id } = req.params;
  try {
    await Post.deletePost(id);
    res.json({ message: "Post deleted successfully" });
  } catch (error) {
    console.error(error.message);
    res.status(500).json({ error: "Server Error" });
  }
};

module.exports = {
  getPosts,
  getPostById,
  createPost,
  updatePost,
  deletePost,
};
