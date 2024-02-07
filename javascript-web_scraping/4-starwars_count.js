#!/usr/bin/node
const url = process.argv[2];
const req = require('request');
req.get(url, (err, body) => {
  if (err) {
    console.log(err);
  } else {
    let times = 0;
    for (const i of JSON.parse(body.body).results) {
      const character = i.characters;
      for (const j of character) {
        if (j.includes('18')) {
          times += 1;
        }
      }
    }
    console.log(times);
  }
});
