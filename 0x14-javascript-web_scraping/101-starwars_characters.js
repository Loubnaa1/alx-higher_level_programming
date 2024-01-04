#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (error, response, body) {
    if (error) console.error('Error:', error);
    else {
    const characters = JSON.parse(body).characters;
    printCharactersname(characters, 0);
  }
});

function printCharactersname (characters, i) {
  request(characters[i], function (error, response, body) {
    if (error) console.error('Error:', error);
    else {
      console.log(JSON.parse(body).name);
      if (i + 1 < characters.length) {
        printCharactersname(characters, i + 1);
      }
    }
  });
}
