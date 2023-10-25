let party = [
  {
    desert: "Chocolate Mousse",
    calories: 30,
  },
  {
    desert: "Apple Pie",
    calories: 15,
  },
  {
    desert: "Croissant",
    calories: 50,
  },
  {
    desert: "Strawberry Icecream",
    calories: 5,
  },
];

let totalCalories = party.reduce((sum, dessert) => {
  if (dessert.desert !== "Apple Pie") {
    return sum + dessert.calories;
  }
  return sum;
}, 0);

console.log(totalCalories);
