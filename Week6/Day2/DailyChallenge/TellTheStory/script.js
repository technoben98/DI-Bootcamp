document.getElementById("libform").addEventListener("submit", function (event) {
  event.preventDefault();
  let noun = document.getElementById("noun").value;
  console.log(noun);
  let adjective = document.getElementById("adjective").value;
  let person = document.getElementById("person").value;
  let verb = document.getElementById("verb").value;
  let place = document.getElementById("place").value;
  if (checkInput(noun, adjective, person, verb, place) == 0) {
    return;
  }

  let story = `${person} went to ${place} and ${verb} a ${adjective} ${noun}.`;

  document.getElementById("story").textContent = story;
});

document
  .getElementById("shuffle-button")
  .addEventListener("click", function () {
    let noun = document.getElementById("noun").value;
    console.log(noun);
    let adjective = document.getElementById("adjective").value;
    let person = document.getElementById("person").value;
    let verb = document.getElementById("verb").value;
    let place = document.getElementById("place").value;
    if (checkInput(noun, adjective, person, verb, place) == 0) {
      return;
    }

    let stories = [
      `Once upon a time, there was a ${adjective} ${noun} named ${person}. ${person} loved to ${verb} in ${place}.`,
      `In a ${place} far away, ${person} discovered a ${adjective} ${noun}. ${person} couldn't resist ${verb} it.`,
      `${person} and their ${noun} went on a ${adjective} adventure. They ${verb} through ${place} and had the time of their lives.`,
      `There was a ${noun} that was so ${adjective}, it made ${person} ${verb} with joy every time they saw it in ${place}.`,
    ];

    let randomStory = stories[Math.floor(Math.random() * stories.length)];

    document.getElementById("story").textContent = randomStory;
  });

function checkInput(noun, adjective, person, verb, place) {
  if (
    noun === "" ||
    adjective === "" ||
    person === "" ||
    verb === "" ||
    place === ""
  ) {
    alert("Please fill in all the inputs");
    return 0;
  }
}
