#!/usr/bin/node
const url = process.argv[2];
const req = require('request');
req.get(url, (err, res, body) => {
  if (err == null) {
    const myObject = {};
    const object = JSON.parse(body);
    for (let i = 0; i < object.length; i++) {
      if (object[i].completed === true) {
        if (myObject[object[i].userId] === undefined) {
          myObject[object[i].userId] = 0;
        }
        myObject[object[i].userId] += 1;
      }
    }
    console.log(myObject);
  }
});
