#!/usr/bin/node
const request = require('request');
const { argv } = require('process');

const options = {
  url: `https://swapi-api.hbtn.io/api/films/${argv[2]}`,
  method: 'GET',
  headers: {
    'Accept-Charset': 'utf-8'
  }
};

request(options, function (err, res, body) {
  if (err) throw err;

  const result = JSON.parse(body).title;
  console.log(result);
});
