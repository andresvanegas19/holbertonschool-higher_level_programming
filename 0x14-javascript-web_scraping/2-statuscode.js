#!/usr/bin/node
const request = require('request');
const { argv } = require('process');

const options = {
  url: argv[2],
  method: 'GET',
  headers: {
    'Accept-Charset': 'utf-8'
  }
};

request(options, function (err, res, body) {
  if (err) throw err;

  if (res) {
    console.log('code: %d', res.statusCode);
  }
});
