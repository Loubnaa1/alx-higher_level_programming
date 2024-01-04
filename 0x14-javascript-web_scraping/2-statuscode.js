#!/usr/bin/node
const request = require('request');
request(process.argv[2], (erreur, response) => {
  if (erreur) console.error(erreur);
  else console.log('code: ' + response.statusCode);
});
