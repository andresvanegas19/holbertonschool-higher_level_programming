#!/usr/bin/node
const request = require('request');
const { argv } = require('process');
const fs = require('fs');

const options = {
  url: argv[2],
  method: 'GET',
  headers: {
    'Accept-Charset': 'utf-8'
  }
};

request(options, function (err, res, body) {
  if (err) throw err;

  fs.writeFile(argv[3], body, function (err) {
    if (err) {
      return console.log(err);
    }
  });
});
