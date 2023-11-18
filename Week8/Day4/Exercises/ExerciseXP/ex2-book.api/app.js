const express = require("express");
const app = express();
const PORT = process.env.PORT || 5000;
require("dotenv").config();

app.use(express.json());

app.use("/api/books", require("./routes/books"));

app.listen(PORT, () => {
  console.log(`Server is running on ${PORT}`);
});
