import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import WeatherPage from "./pages/WeatherPage";
import FavoritesPage from "./pages/FavoritesPage";
import Navbar from "./components/Navbar";
import "./App.css";

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <Switch>
          <Route path="/" exact component={WeatherPage} />
          <Route path="/favorites" component={FavoritesPage} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
