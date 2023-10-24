let client = "John";

const groceries = {
  fruits: ["pear", "apple", "banana"],
  vegetables: ["tomatoes", "cucumber", "salad"],
  totalPrice: "20$",
  other: {
    paid: true,
    meansOfPayment: ["cash", "creditCard"],
  },
};

let displayGroceries = () => {
  groceries.fruits.forEach((fruit) => {
    console.log(fruit);
  });
};

displayGroceries();

let cloneGroceries = () => {
  let user = client;
  console.log(user === client);
  client = "Betty"; // we dont see modification in user too, because that user and client it's primitive data type and they cant modificate one to one
  console.log(user);
  console.log(client);
  console.log(user === client);

  let shopping = groceries;
  shopping.totalPrice = "35$"; //this line modificate shopping and groceries too because of object it's not primitive type of data. it's the same object in one cluster of memory and when we create shopping we only give hime link to this cluster. So this two variable link to one object and they can modificate them.
  console.log(shopping.totalPrice);
  console.log(groceries.totalPrice);
  console.log(shopping === groceries);
};

cloneGroceries();
