#!/usr/bin/node
const request = require('request');
const argument = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
request(url + argument, (erreur, response, body) => {
  if (erreur) console.log(erreur);
  if (response.statusCode === 200) {
    const response = JSON.parse(body);
    console.log(response.title);
  }
});
