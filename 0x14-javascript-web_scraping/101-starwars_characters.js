#!/usr/bin/node
const request = require('request');

function processCharacters(characters, index) {
  if (index >= characters.length) {
    return;
  }

  request(characters[index], (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }

    console.log(JSON.parse(body).name);
    processCharacters(characters, index + 1);
  });
}

const Url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(Url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  const characters = JSON.parse(body).characters;
  processCharacters(characters, 0);
});
