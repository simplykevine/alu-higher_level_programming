#!/usr/bin/node
const movieId = process.argv.slice(2)[0];
const request = require('request');

const filmsUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(filmsUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const parseData = JSON.parse(body);
    const characters = parseData.characters;
    characters.forEach(charUrl => {
      request(charUrl, (err, response, body) => {
        if (err) console.log(err);
        else {
          const parseCharData = JSON.parse(body);
          console.log(parseCharData.name);
        }
      });
    });
  }
});
