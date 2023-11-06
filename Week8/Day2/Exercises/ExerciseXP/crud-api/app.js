const express = require("express");
const axios = require("axios");
const app = express();

// Set up the app to listen on port 5000
const port = 5000;
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});

// Import the dataService module
const dataService = require("./data/dataService.js");

// Create an endpoint to fetch data from the JSONPlaceholder API
app.get("/api/posts", async (req, res) => {
  try {
    // Use the fetchPosts function from the dataService module
    const posts = await dataService.fetchPosts();

    // Send the fetched data as a response
    res.json(posts);

    // Print a success message in the console
    console.log("Data fetched and sent successfully");
  } catch (error) {
    // Handle any errors that occurred during the data retrieval process
    console.error("Error fetching data:", error);
    res.sendStatus(500);
  }
});
//
