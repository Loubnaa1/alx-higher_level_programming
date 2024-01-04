#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';

request(url + process.argv[2], (error, response, body) => {
  if (error) console.log(error);
  else {
    const characters = JSON.parse(body).characters;
    let index = 0;

    while (index < characters.length) {
      const ch1 = characters[index];
      request(ch1, (error, response, body) => {
        if (error) console.log(error);
        else {
          const chData1 = JSON.parse(body);
          console.log(chData1.name);
        }
      });
      index++;
    }
  }
});
