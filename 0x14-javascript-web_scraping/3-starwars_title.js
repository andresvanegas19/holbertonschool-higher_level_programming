#!/usr/bin/env node
const request = require('request');
const { argv } = require('process');

const options = {
    url: `https://swapi-api.hbtn.io/api/films/${argv[2]}`,
    method: 'GET',
    headers: {
        'Accept-Charset': 'utf-8',
    }
};

request(options, function(err, res, body) {
  console.log(JSON.parse(body)['title'])
});
