#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
request(url + process.argv[2], (error, response, body) => {
  if (error) {
	  console.error('Error:', error);
	  }
  else {
    const caracters = JSON.parse(body).characters;
    printcaract(caracters, 0);
  }
});
function printcaract (caracters, index) {
  request(caracters[index], (error, response, body) => {
    if (error) {
	    console.error(error);
	    }
    else {
      console.log(JSON.parse(body).name);
      if (index + 1 < caracters.length) {
        printcaract(caracters, index + 1);
      }
    }
  });
}
