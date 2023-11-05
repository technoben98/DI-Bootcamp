// 🌟 Exercise 3: File Management Using CommonJS Syntax

const { readFile, writeFile } = require("./fileManager.cjs");

readFile("Hello World.txt");

writeFile("Bye World.txt", "Writing to the file");
