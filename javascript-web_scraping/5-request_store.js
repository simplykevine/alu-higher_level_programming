#!/usr/bin/node
const url = process.argv[2];
const fileName = process.argv[3];
const req = require('request');
const fs = require('fs');
req.get(url, (err, res, body) => {
  if (err == null) {
    fs.writeFile(fileName, body, 'utf8', err => {
      if (err) {
        console.log(err);
      }
    });
  }
});
