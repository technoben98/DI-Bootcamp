const express = require("express");
const app = express();
const cors = require("cors");
const PORT = 5000;

app.use(cors());
app.use(express.json());

app.get("/api/hello", (req, res) => {
  res.json({ message: "Hello From Express" });
});

app.post("/api/world", (req, res) => {
  const clientMessage = req.body.value;
  console.log("Message from client:", clientMessage);

  const serverResponse = `I received your POST request. This is what you sent me: ${clientMessage}`;
  res.json({ message: serverResponse });
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
