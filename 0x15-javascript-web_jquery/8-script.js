$.get("https://swapi-api.hbtn.io/api/films/?format=json", (data) => {
  data.results.forEach(element => {
    $('UL#list_movies').prepend($("<li></li>").text(element.title));
  });
})
