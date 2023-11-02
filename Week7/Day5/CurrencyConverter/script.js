const apiKey = "a9c1a925a238bd9446552a28";
const fromCurrencySelect = document.getElementById("fromCurrency");
const toCurrencySelect = document.getElementById("toCurrency");
const amountInput = document.getElementById("amount");
const convertBtn = document.getElementById("convertBtn");
const resultElement = document.getElementById("result");
const switchBtn = document.getElementById("switchBtn");

fetch(`https://v6.exchangerate-api.com/v6/${apiKey}/codes`)
  .then((response) => response.json())
  .then((data) => {
    const supportedCurrencies = data.supported_codes;
    supportedCurrencies.forEach((currency) => {
      const option1 = document.createElement("option");
      option1.value = currency[0];
      option1.textContent = currency;
      const option2 = document.createElement("option");
      option2.value = currency[0];
      option2.textContent = currency;
      fromCurrencySelect.appendChild(option1);
      toCurrencySelect.appendChild(option2);
    });
  })
  .catch((error) => console.log(error));

// Convert currency
convertBtn.addEventListener("click", () => {
  const fromCurrency = fromCurrencySelect.value;
  const toCurrency = toCurrencySelect.value;
  const amount = parseFloat(amountInput.value);
  const conversionUrl = `https://v6.exchangerate-api.com/v6/${apiKey}/pair/${fromCurrency}/${toCurrency}/${amount}`;

  fetch(conversionUrl)
    .then((response) => response.json())
    .then((data) => {
      const convertedAmount = data.conversion_result;
      resultElement.textContent = `${amount} ${fromCurrency} = ${convertedAmount} ${toCurrency}`;
    })
    .catch((error) => console.log(error));
});

switchBtn.addEventListener("click", () => {
  const temp = fromCurrencySelect.value;
  fromCurrencySelect.value = toCurrencySelect.value;
  toCurrencySelect.value = temp;
});
