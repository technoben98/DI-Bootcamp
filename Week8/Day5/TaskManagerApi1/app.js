const express = require("express");
const bodyParser = require("body-parser");
const tasksRouter = require("./routes/tasks");

const app = express();
const PORT = process.env.PORT || 3000;

app.use(bodyParser.json());

// Routes
app.use("/tasks", tasksRouter);

app.listen(PORT, () => {
  console.log(`Server is running on ${PORT}`);
});
