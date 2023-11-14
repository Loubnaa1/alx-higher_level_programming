#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const t = add(Number(process.argv[2]), Number(process.argv[3]));
console.log(t);
