// Function to handle registration form submission
async function registerUser() {
  const name = document.getElementById("name").value;
  const lastName = document.getElementById("lastName").value;
  const email = document.getElementById("email").value;
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  const response = await fetch("http://localhost:3000/user/register", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ name, lastName, email, username, password }),
  });

  const result = await response.json();
  alert(result.message);
}

// Function to handle login form submission
async function loginUser() {
  const username = document.getElementById("loginUsername").value;
  const password = document.getElementById("loginPassword").value;

  const response = await fetch("http://localhost:3000/user/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ username, password }),
  });

  const result = await response.json();
  alert(result.message);
}

// Function to retrieve all users (for demonstration purposes)
async function getAllUsers() {
  const response = await fetch("http://localhost:3000/user/users");
  const users = await response.json();
  console.log(users);
}

// Function to retrieve a specific user by ID (for demonstration purposes)
async function getUserById(id) {
  const response = await fetch(`http://localhost:3000/user/users/${id}`);
  const user = await response.json();
  console.log(user);
}

// Function to update a user by ID (for demonstration purposes)
async function updateUserById(id) {
  const name = prompt("Enter updated name:");
  const lastName = prompt("Enter updated last name:");
  const email = prompt("Enter updated email:");

  const response = await fetch(`http://localhost:3000/user/users/${id}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ name, lastName, email }),
  });

  const result = await response.json();
  console.log(result);
}
