#!/usr/bin/node
const request = require('request');
let count = 0;
request(process.argv[2], (error, response, body) => {
  if (error) console.error(error);
  else {
    const results = JSON.parse(body).results;
    count = results.reduce((count, object) => {
      return count + object.characters.find(character => character.endsWith('/18/'));
    }, count);
  }
  console.log(count);
});