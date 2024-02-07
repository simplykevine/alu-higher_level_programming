#!/usr/bin/node
const url = process.argv[2];
const req = require('request');
req.get(url, (err, res) => {
  if (err) {
    console.log('code: ' + err);
  }

  console.log('code: ' + res.statusCode);
});
