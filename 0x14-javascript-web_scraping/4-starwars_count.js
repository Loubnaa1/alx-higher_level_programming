#!/usr/bin/node
const request = require('request');
let count = 0;
request(process.argv[2], (error, response, body) => {
  if (error) console.error(error);
  else {
    const results = JSON.parse(body).results;
    for (let object of results) {
      for (let character of object.characters) {
        if (character.endsWith('/18/')) {
          count++;
          break; // Exit the inner loop once a matching character is found
        }
      }
    }

    console.log(count);
  }
});

