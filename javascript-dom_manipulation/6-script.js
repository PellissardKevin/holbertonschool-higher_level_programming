fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")
  .then(response => response.json())
  .then(characters => showCharacters(characters));

function showCharacters(characters) {
  const charactersDiv = document.querySelector("#character");
  charactersDiv.innerText = `${characters.name}`;
  charactersDiv.append(characterElement);
};





