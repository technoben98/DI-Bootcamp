const express = require("express");
const app = express();
// const cors = require("cors");
const dotenv = require("dotenv");
// dotenv.config();

app.use(express.json());

// Routes
app.use("/posts", require("./routes/posts"));

app.listen(process.env.PORT, () => {
  console.log(`Listen on port ${process.env.PORT}`);
});
