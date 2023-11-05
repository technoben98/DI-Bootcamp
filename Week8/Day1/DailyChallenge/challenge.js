import { greet } from "./greeting.js";
import { displayColorfulMessage } from "./colorful-message.js";
import { readFileData } from "./files/read-file.js";

const name = "user";
greet(name);
displayColorfulMessage();
readFileData("./files/file-data.txt");
