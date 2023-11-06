// const winCombos = [
//   [0, 1, 2],
//   [3, 4, 5],
//   [6, 7, 8],
//   [0, 3, 6],
//   [1, 4, 7],
//   [2, 5, 8],
//   [0, 4, 8],
//   [6, 4, 2],
// ];

// let currentPlayer;
// let playerSymbol;
// let computerSymbol;
// let board;
// let gameEnded;

// function startGame() {
//   currentPlayer = "player";
//   playerSymbol = "";
//   computerSymbol = "";
//   board = ["", "", "", "", "", "", "", "", ""];
//   gameEnded = false;
//   document.querySelectorAll(".box").forEach((box) => {
//     box.textContent = "";
//     box.addEventListener("click", playerTurn);
//   });
//   getPlayerSymbol();
// }

// function getPlayerSymbol() {
//   const symbolButtons = document.querySelectorAll("[data-symbol]");
//   symbolButtons.forEach((button) => {
//     button.addEventListener("click", () => {
//       playerSymbol = button.dataset.symbol;
//       computerSymbol = playerSymbol === "X" ? "O" : "X";
//       startGame();
//     });
//   });
// }

// function playerTurn() {
//   const boxIndex = parseInt(this.id.substring(3));
//   if (board[boxIndex] === "" && currentPlayer === "player") {
//     board[boxIndex] = playerSymbol;
//     this.textContent = playerSymbol;
//     currentPlayer = "computer";
//     checkOutcome();
//     if (!gameEnded) {
//       setTimeout(computerTurn, 500);
//     }
//   }
// }

// function computerTurn() {
//   const emptyBoxes = board.reduce((acc, box, index) => {
//     if (box === "") {
//       acc.push(index);
//     }
//     return acc;
//   }, []);

//   const randomIndex = Math.floor(Math.random() * emptyBoxes.length);
//   const boxIndex = emptyBoxes[randomIndex];

//   board[boxIndex] = computerSymbol;
//   document.getElementById(`box${boxIndex}`).textContent = computerSymbol;
//   currentPlayer = "player";
//   checkOutcome();
// }

// function checkOutcome() {
//   const playerBoxes = board.reduce((acc, box, index) => {
//     if (box === playerSymbol) {
//       acc.push(index);
//     }
//     return acc;
//   }, []);

//   const computerBoxes = board.reduce((acc, box, index) => {
//     if (box === computerSymbol) {
//       acc.push(index);
//     }
//     return acc;
//   }, []);

//   let gameWon = false;
//   let winningCombo;

//   for (const combo of winCombos) {
//     if (combo.every((elem) => playerBoxes.includes(elem))) {
//       gameWon = true;
//       winningCombo = combo;
//       break;
//     } else if (combo.every((elem) => computerBoxes.includes(elem))) {
//       gameWon = true;
//       winningCombo = combo;
//       break;
//     }
//   }
//   if (gameWon) {
//     gameEnded = true;
//     highlightWinningCombo(winningCombo);
//     const winner = currentPlayer === "player" ? "Player" : "Computer";
//     document.querySelector("h1").textContent = `${winner} Wins!`;
//   } else if (board.every((box) => box !== "")) {
//     gameEnded = true;
//     document.querySelector("h1").textContent = "Tie Game!";
//   }
// }

// function highlightWinningCombo(winningCombo) {
//   winningCombo.forEach((index) => {
//     document.getElementById(`box${index}`).style.backgroundColor = "#99ff99";
//   });
// }

// function restartGame() {
//   document.querySelectorAll(".box").forEach((box) => {
//     box.textContent = "";
//     box.style.backgroundColor = "lightgray";
//     box.removeEventListener("click", playerTurn);
//   });

//   document.querySelector("h1").textContent = "Tic Tac Toe";

//   startGame();
// }

// startGame();
