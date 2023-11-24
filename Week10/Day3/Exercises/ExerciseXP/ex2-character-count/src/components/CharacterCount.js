import React, { useRef } from "react";

function CharacterCounter() {
  const inputRef = useRef(null);

  const handleInputChange = () => {
    const textLength = inputRef.current.value.length;
    document.getElementById("character-count").textContent = textLength;
  };

  return (
    <div>
      <h1>Character Counter</h1>
      <textarea
        ref={inputRef}
        onChange={handleInputChange}
        placeholder="Type something..."
      ></textarea>
      <p>
        Character Count: <span id="character-count">0</span>
      </p>
    </div>
  );
}

export default CharacterCounter;
