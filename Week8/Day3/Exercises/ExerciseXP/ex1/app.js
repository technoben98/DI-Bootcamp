const express = require("express");
const app = express();
const PORT = 3000;

// Import the router module
const routes = require("./routes");

// Mount the router
app.use("/", routes);

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
