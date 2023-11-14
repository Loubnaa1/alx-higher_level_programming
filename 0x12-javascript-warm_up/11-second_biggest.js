#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const second = process.argv.slice(2).sort((a, b) => a - b);
  console.log(second[second.length - 2]);
}
