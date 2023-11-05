const _ = require("lodash");
const math = require("./math");

const sum = math.add(5, 3);
const product = math.multiply(4, 2);
const max = _.max([1, 2, 3, 4, 5]);

console.log("Sum:", sum);
console.log("Product:", product);
console.log("Max:", max);
