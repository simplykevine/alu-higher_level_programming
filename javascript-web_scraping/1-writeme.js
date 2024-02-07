#!/usr/bin/node
const myFile = process.argv[2];
const content = process.argv[3];
const fs = require('fs');
fs.writeFile(myFile, content, err => {
  if (err) {
    console.log(err);
  }
});
