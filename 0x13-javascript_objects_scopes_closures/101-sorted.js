#!/usr/bin/node
const dict = require('./101-data.js').dict;
const dictionn = {};
for (const key in dict) {
  if (dictionn[dict[key]] === undefined) {
    dictionn[dict[key]] = [key];
  } else {
    dictionn[dict[key]].push(key);
  }
}
console.log(dictionn);
