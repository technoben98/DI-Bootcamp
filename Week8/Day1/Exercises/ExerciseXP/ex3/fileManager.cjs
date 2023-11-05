const fs = require("fs");

function readFile(filePath) {
  try {
    const content = fs.readFileSync(filePath, "utf-8");
    console.log(`Read file content: ${content}`);
  } catch (error) {
    console.log(`Error reading file: ${error}`);
  }
}

function writeFile(filePath, content) {
  try {
    fs.writeFileSync(filePath, content, "utf-8");
    console.log(`Successfully wrote to file: ${filePath}`);
  } catch (error) {
    console.log(`Error writing to file: ${error}`);
  }
}

module.exports = { readFile, writeFile };
