#!/usr/bin/node
const num = process.argv[2];
const req = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
req.get(url + num, (err, res, body) => {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    console.log(JSON.parse(body).title);
  }
});
