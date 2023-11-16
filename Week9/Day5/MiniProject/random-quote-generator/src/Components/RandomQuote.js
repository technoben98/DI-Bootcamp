import React, { useState } from "react";
import quotes from "./QuotesDb.js";

const getRandomQuote = (currentQuote) => {
  let randomIndex = Math.floor(Math.random() * quotes.length);
  while (quotes[randomIndex].quote === currentQuote) {
    randomIndex = Math.floor(Math.random() * quotes.length);
  }
  return quotes[randomIndex];
};

const getRandomColor = () => {
  const letters = "0123456789ABCDEF";
  let color = "#";
  for (let i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
};

const RandomQuote = () => {
  const [quote, setQuote] = useState(getRandomQuote(""));
  const [backgroundColor, setBackgroundColor] = useState(getRandomColor());
  const [quoteColor, setQuoteColor] = useState(getRandomColor());
  const [buttonColor, setButtonColor] = useState(getRandomColor());

  const generateRandomQuote = () => {
    const newQuote = getRandomQuote(quote.quote);
    setQuote(newQuote);
    setBackgroundColor(getRandomColor());
    setQuoteColor(getRandomColor());
    setButtonColor(getRandomColor());
  };

  return (
    <div
      style={{
        background: backgroundColor,
        height: "89vh",
        paddingTop: "100px",
      }}
    >
      <div
        style={{
          background: "white",
          padding: "20px",
          textAlign: "center",
          width: "60vw",
          margin: "auto",
        }}
      >
        <h1
          style={{
            color: quoteColor,
            fontSize: "24px",
          }}
        >
          {quote.quote}
        </h1>
        <p>{quote.author}</p>
        <button
          style={{
            background: buttonColor,
            color: "#FFFFFF",
            padding: "8px 16px",
            border: "none",
            borderRadius: "4px",
            marginLeft: "400px",
          }}
          onClick={generateRandomQuote}
        >
          Generate Quote
        </button>
      </div>
    </div>
  );
};

export default RandomQuote;
