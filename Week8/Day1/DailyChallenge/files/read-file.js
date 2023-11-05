const fs = require("fs");
const filePath = "./file-data.txt";
const readFileData = (filePath) => {
  fs.readFile(filePath, "utf8", (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(data);
  });
};

module.exports = { readFileData };
