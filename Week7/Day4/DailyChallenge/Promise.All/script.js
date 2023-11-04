document.getElementById("cityForm").addEventListener("submit", function (e) {
  e.preventDefault();

  let city1Lat = document.getElementById("city1Lat").value;
  let city1Lng = document.getElementById("city1Lng").value;
  let city2Lat = document.getElementById("city2Lat").value;
  let city2Lng = document.getElementById("city2Lng").value;

  let apiUrl = `https://api.sunrise-sunset.org/json?lat={LAT}&lng={LNG}&date=today`;

  let city1ApiUrl = `https://api.sunrise-sunset.org/json?lat=${city1Lat}&lng=${city1Lng}&date=today`;
  let city2ApiUrl = `https://api.sunrise-sunset.org/json?lat=${city2Lat}&lng=${city2Lng}&date=today`;

  let city1DataPromise = fetch(city1ApiUrl).then((response) => response.json());
  let city2DataPromise = fetch(city2ApiUrl).then((response) => response.json());

  Promise.all([city1DataPromise, city2DataPromise])
    .then(function (results) {
      let city1Sunrise = results[0].results.sunrise;
      let city2Sunrise = results[1].results.sunrise;

      let resultsContainer = document.getElementById("resultsContainer");
      resultsContainer.innerHTML = `
          <p>City 1 Sunrise: ${city1Sunrise}</p>
          <p>City 2 Sunrise: ${city2Sunrise}</p>
        `;
    })
    .catch(function (error) {
      console.error("Error:", error);
    });
});
