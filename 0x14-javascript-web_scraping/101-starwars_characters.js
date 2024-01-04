#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';

request(url + process.argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const characters = JSON.parse(body).characters;
    printCharacterNames(characters, 0);
  }
});

function printCharacterNames(characters, i) {
  if (i >= characters.length) {
    return;
  }

  request(characters[i], (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }

    console.log(JSON.parse(body).name);
    printCharacterNames(characters, i + 1);
  });
}
