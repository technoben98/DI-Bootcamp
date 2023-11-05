// 🌟 Exercise 2: Advanced Module Usage Using ES6 Module Syntax

import persons from "./data.js";

function calculateAverageAge(persons) {
  const totalAge = persons.reduce((sum, person) => sum + person.age, 0);
  const averageAge = totalAge / persons.length;

  console.log(`Average Age: ${averageAge}`);
}

calculateAverageAge(persons);
