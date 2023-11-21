import { BrowserRouter, Routes, Route, NavLink } from "react-router-dom";
import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";

// Exercise 1

// import ErrorBoundary from "./Components/ErrorBoundary.js";

// const HomeScreen = () => <h1>Home</h1>;
// const ProfileScreen = () => <h1>Profile</h1>;
// const ShopScreen = () => {
//   throw new Error("Error in ShopScreen");
// };

// function App() {
//   return (
//     <BrowserRouter>
//       <nav className="navbar navbar-expand-lg navbar-light bg-light">
//         <div className="container">
//           <NavLink className="navbar-brand" to="/">
//             Home
//           </NavLink>
//           <NavLink className="nav-link" to="/profile">
//             Profile
//           </NavLink>
//           <NavLink className="nav-link" to="/shop">
//             Shop
//           </NavLink>
//         </div>
//       </nav>

//       <div className="container mt-4">
//         <Routes>
//           <Route
//             path="/"
//             element={
//               <ErrorBoundary>
//                 <HomeScreen />
//               </ErrorBoundary>
//             }
//           />
//           <Route
//             path="/profile"
//             element={
//               <ErrorBoundary>
//                 <ProfileScreen />
//               </ErrorBoundary>
//             }
//           />
//           <Route
//             path="/shop"
//             element={
//               <ErrorBoundary>
//                 <ShopScreen />
//               </ErrorBoundary>
//             }
//           />
//         </Routes>
//       </div>
//     </BrowserRouter>
//   );
// }

// Exercise 2

// import React from "react";
// import PostList from "./Components/PostList.js";

// function App() {
//   return (
//     <div className="container mt-4">
//       {/* Render the PostList component */}
//       <PostList />
//     </div>
//   );
// }

// Exercise 3

// import React from "react";
// import Example1 from "./Components/Example1";
// import Example2 from "./Components/Example2";
// import Example3 from "./Components/Example3";
// import data from "./data/students.json";

// function App() {
//   return (
//     <div className="container mt-4">
//       {/* Render the Example components with data */}
//       <Example1 data={data} />
//       <Example2 data={data} />
//       <Example3 data={data} />
//     </div>
//   );
// }

// Exercise 4

import React, { useState } from "react";

function App() {
  const [response, setResponse] = useState(null);

  const handleClick = async () => {
    const url = "https://webhook.site/713136a7-549f-4ddd-832f-0cd735c595dc";
    const jsonData = {
      key1: "myusername",
      email: "mymail@gmail.com",
      name: "Isaac",
      lastname: "Doe",
      age: 27,
    };

    try {
      const response = await fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(jsonData),
      });

      const data = await response.json();
      setResponse(data);
      console.log("Webhook Response:", data);
    } catch (error) {
      console.error("Error sending POST request:", error);
    }
  };

  return (
    <div className="container mt-4">
      <button onClick={handleClick}>Send POST Request</button>

      {response && (
        <div>
          <h2>Response from Webhook</h2>
          <pre>{JSON.stringify(response, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
