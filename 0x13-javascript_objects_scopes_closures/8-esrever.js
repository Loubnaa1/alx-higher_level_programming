#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;
  let i = 0;
  while (len > 0 && len > i) {
    const num = list[len];
    list[len] = list[n];
    list[n] = num;
    i++;
    len--;
  }
  return list;
};
