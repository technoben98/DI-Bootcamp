const fs = require("fs");
const path = require("path");

const tasksFilePath = path.join(__dirname, "../data/tasks.json");

const readTasksFile = () => {
  const tasksData = fs.readFileSync(tasksFilePath, "utf-8");
  return JSON.parse(tasksData);
};

const writeTasksFile = (tasks) => {
  fs.writeFileSync(tasksFilePath, JSON.stringify(tasks, null, 2), "utf-8");
};

const getAllTasks = (req, res) => {
  try {
    const tasks = readTasksFile();
    res.json(tasks);
  } catch (error) {
    console.error(error.message);
    res.status(500).json({ error: "Server Error" });
  }
};

const getTaskById = (req, res) => {
  const { id } = req.params;
  try {
    const tasks = readTasksFile();
    const task = tasks.find((task) => task.id === parseInt(id));
    if (task) {
      res.json(task);
    } else {
      res.status(404).json({ error: "Task not found" });
    }
  } catch (error) {
    console.error(error.message);
    res.status(500).json({ error: "Server Error" });
  }
};

const createTask = (req, res) => {
  const { title, description } = req.body;
  try {
    if (!title || !description) {
      return res
        .status(400)
        .json({ error: "Title and description are required" });
    }

    const tasks = readTasksFile();
    const newTask = {
      id: tasks.length + 1,
      title,
      description,
    };

    tasks.push(newTask);
    writeTasksFile(tasks);
    res.json(newTask);
  } catch (error) {
    console.error(error.message);
    res.status(500).json({ error: "Server Error" });
  }
};

const updateTask = (req, res) => {
  const { id } = req.params;
  const { title, description } = req.body;
  try {
    if (!title || !description) {
      return res
        .status(400)
        .json({ error: "Title and description are required" });
    }

    const tasks = readTasksFile();
    const taskIndex = tasks.findIndex((task) => task.id === parseInt(id));

    if (taskIndex !== -1) {
      tasks[taskIndex] = {
        id: parseInt(id),
        title,
        description,
      };

      writeTasksFile(tasks);
      res.json(tasks[taskIndex]);
    } else {
      res.status(404).json({ error: "Task not found" });
    }
  } catch (error) {
    console.error(error.message);
    res.status(500).json({ error: "Server Error" });
  }
};

const deleteTask = (req, res) => {
  const { id } = req.params;
  try {
    const tasks = readTasksFile();
    const updatedTasks = tasks.filter((task) => task.id !== parseInt(id));

    if (tasks.length !== updatedTasks.length) {
      writeTasksFile(updatedTasks);
      res.json({ message: "Task deleted successfully" });
    } else {
      res.status(404).json({ error: "Task not found" });
    }
  } catch (error) {
    console.error(error.message);
    res.status(500).json({ error: "Server Error" });
  }
};

module.exports = {
  getAllTasks,
  getTaskById,
  createTask,
  updateTask,
  deleteTask,
};
