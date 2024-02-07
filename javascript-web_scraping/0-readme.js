#!/usr/bin/node
const myFile = process.argv[2];
const fs = require('fs');
fs.readFile(myFile, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  }

  console.log(data);
});
