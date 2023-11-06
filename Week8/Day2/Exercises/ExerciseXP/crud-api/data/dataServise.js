const axios = require("axios");

// Function to fetch data from the JSONPlaceholder API
const fetchPosts = async () => {
  try {
    // Make a GET request to the JSONPlaceholder API
    const response = await axios.get(
      "https://jsonplaceholder.typicode.com/posts"
    );

    // Return the response data from the API
    return response.data;
  } catch (error) {
    // Handle any errors that occurred during the data retrieval process
    throw new Error("Error fetching posts");
  }
};

// Export the fetchPosts function
module.exports = {
  fetchPosts,
};
