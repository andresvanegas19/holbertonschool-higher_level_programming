#!/usr/bin/env node
const request = require('request');
const { argv } = require('process');

const options = {
    url: `https://swapi-api.hbtn.io/api/films/${argv[2]}/`,
    method: 'GET',
    headers: {
        'Accept-Charset': 'utf-8',
    }
};

request(options, function(err, res, body) {
  const characters = JSON.parse(body).characters;

  characters.forEach(element => {
    request(element, function(err, res, _body) {
      console.log(JSON.parse(_body).name)
    })
  });

});
