fetch("https://swapi-api.hbtn.io/api/films/?format=json")
  .then(response => response.json())
  .then(movies => listTitle(movies.results));

function listTitle(movies) {
  movies.forEach(title => {
    const listDiv = document.querySelector("#list_movies");
    const listElement = document.createElement('li');
    listElement.innerText = `${title.title}`;
    listDiv.append(listElement);
  });
};

