#!/usr/bin/env node
const request = require('request');
const { argv } = require('process');

const options = {
    url: argv[2],
    method: 'GET',
    headers: {
        'Accept-Charset': 'utf-8',
    }
};

request(options, function(err, res, body) {
  const result = JSON.parse(body)
  const dict = {};

  result.forEach(element => {
    let userId = element['userId']
    if (!dict[userId]) {
      dict[userId] = 0
    }

    if (element['completed'] === true) {
      dict[userId] += 1
    }
  });
  console.log(dict)
});
