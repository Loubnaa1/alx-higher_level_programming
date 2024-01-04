#!/usr/bin/node
const request = require('request');

request(process.argv[2], (error, response, body) => {
  let count = 0;

  if (error) {
    console.error(error);
  } else {
    const results = JSON.parse(body).results;

    for (let i = 0; i < results.length; i++) {
      for (let j = 0; j < results[i].characters.length; j++) {
        if (results[i].characters[j].includes('18')) {
          count++;
        }
      }
    }
  }

  console.log(count);
});
