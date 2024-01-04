#!/usr/bin/node
const request = require('request');
let count = 0;
request(process.argv[2], (error, response, body) => {
  if (error) console.error(error);
  else {
    const results = JSON.parse(body).results;
    console.log(results.filter(object => object.characters.some(character => character.endsWith('/18/'))
  ).length);
  }
  console.log(count);
});
