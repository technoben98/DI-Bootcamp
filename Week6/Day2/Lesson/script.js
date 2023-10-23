// const table = document.getElementById("sampleTable");
// let rowPos = 2;

// function insertRow(){
//     rowPos++;
//     const row = document.createElement("tr");
//     const td1 = document.createElement("td");
//     const td2 = document.createElement("td");
//     td1.textContent = `Row${rowPos} cell1`;
//     td2.textContent = `Row${rowPos} cell2`;
//     table.append(row);
//     row.append(td1,td2);
// }

const button = document.getElementById("jsstyle");
const div = document.querySelector("div");

button.addEventListener("click", function () {
  button.style.color = "blue";
});

button.addEventListener("click", function (e) {
  button.style.border = "3px dotted green";
  e.stopPropagation();
});

div.addEventListener("click", function () {
  alert("div is clicked");
});
