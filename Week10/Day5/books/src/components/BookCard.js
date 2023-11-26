import React from "react";

const BookCard = ({ book }) => {
  return (
    <div className="cards">
      <img src={book.image} alt={book.title} />
      <h3>{book.title}</h3>
      <p>{book.authors.join(", ")}</p>
      <p>{book.publishedDate}</p>
    </div>
  );
};

export default BookCard;
