#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', (erreur, content) => {
  if (erreur) console.error(erreur);
  else console.log(content);
});
