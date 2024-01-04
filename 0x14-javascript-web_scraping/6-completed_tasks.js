#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const tasks = JSON.parse(body);
    const counts = tasks.reduce((sum, task) => {
      if (task.completed) {
        sum[task.userId] = (sum[task.userId] || 0) + 1;
      }
      return sum;
    }, {});

    console.log(counts);
  }
});

