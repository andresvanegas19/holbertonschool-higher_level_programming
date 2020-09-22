#!/usr/bin/node
const request = require('request');
const { argv, exit } = require('process');

const options = {
    url: argv[2],
    method: 'GET',
    headers: {
        'Accept-Charset': 'utf-8',
    }
};

request(options, function(err, res, body) {
  if (res) {
   console.log('code: %d', res.statusCode);
  }
});
