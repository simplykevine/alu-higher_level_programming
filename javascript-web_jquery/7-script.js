#!/usr/bin/node
$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
  $('div#character').text(data.name);
});
