import React from "react";

const SearchBox = ({ searchTerm, onSearchTermChange, onSearch }) => {
  return (
    <div className="search">
      <input
        type="text"
        value={searchTerm}
        onChange={(e) => onSearchTermChange(e.target.value)}
      />
      <button onClick={onSearch}>Search</button>
    </div>
  );
};

export default SearchBox;
