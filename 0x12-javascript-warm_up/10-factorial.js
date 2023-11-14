#!/usr/bin/node
function factorial (y) {
  if (y === 0 || isNaN(y)) {
    return (1);
  } else if (y < 0) {
    return (-1);
  }
  return (y * factorial(y - 1));
}

console.log(factorial(parseInt(process.argv[2])));
