import React, { useState } from "react";
import Header from "./components/Header";
import SearchBox from "./components/SearchBox";
import BookList from "./components/BookList";
import "./App.css";

const App = () => {
  const [searchTerm, setSearchTerm] = useState("");
  const [books, setBooks] = useState([]);

  const handleSearch = async () => {
    try {
      const response = await fetch(
        `https://www.googleapis.com/books/v1/volumes?q=${searchTerm}`
      );
      const data = await response.json();

      const bookData = data.items.map((item) => ({
        id: item.id,
        title: item.volumeInfo.title,
        authors: item.volumeInfo.authors,
        publishedDate: item.volumeInfo.publishedDate,
        image: item.volumeInfo.imageLinks?.thumbnail,
      }));

      setBooks(bookData);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  return (
    <div>
      <Header title="Search Book App" />
      <SearchBox
        searchTerm={searchTerm}
        onSearchTermChange={(value) => setSearchTerm(value)}
        onSearch={handleSearch}
      />
      <BookList books={books} />
    </div>
  );
};

export default App;
