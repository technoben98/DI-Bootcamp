function submitForm(event) {
  event.preventDefault();

  const name = document.getElementById("name").value;
  const lastName = document.getElementById("last-name").value;

  const data = {
    name,
    lastName,
  };

  const jsonString = JSON.stringify(data);

  const outputElement = document.getElementById("output");
  outputElement.textContent = jsonString;
}
