const fs = require("fs");

const directoryPath = "./";

fs.readdir(directoryPath, (err, files) => {
  if (err) {
    console.error(err);
  } else {
    files.forEach((file) => {
      console.log(file);
    });
  }
});
