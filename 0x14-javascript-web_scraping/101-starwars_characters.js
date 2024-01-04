#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
request(url + process.argv[2], (error, response, body) => {
  if (error) console.error(error);
  else {
    const car = JSON.parse(body).characters;
    printcar(car, 0);
  }
});
function printcar (car, i) {
  request(car[i], (error, response, body) => {
    if (error) console.error(error);
    else {
      console.log(JSON.parse(body).name);
      if (i + 1 < car.length) {
        printcar(car, i + 1);
      }
    }
  });
}
