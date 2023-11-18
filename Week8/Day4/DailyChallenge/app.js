const express = require("express");
const app = express();
const PORT = process.env.PORT || 3000;
require("dotenv").config();
const db = require("./config/knex");
const routes = require("./routes/routes");

app.use(express.json());

app.use((req, res, next) => {
  req.db = db;
  next();
});

app.use("/api", routes);

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
