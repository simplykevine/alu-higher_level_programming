#!/usr/bin/node
const movieId = process.argv.slice(2)[0];
const request = require('request');

const filmsUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;

function printCharacterName (characters, index) {
  request(characters[index], (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      const name = JSON.parse(body).name;
      console.log(name);
      if (index < characters.length - 1) {
        printCharacterName(characters, index + 1);
      }
    }
  });
}

request(filmsUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const parseData = JSON.parse(body);
    const characters = parseData.characters;
    printCharacterName(characters, 0);
  }
});
