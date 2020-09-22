#!/usr/bin/node
const request = require('request');
const { argv } = require('process');

const options = {
    url: argv[2],
    method: 'GET',
    headers: {
        'Accept-Charset': 'utf-8',
    }
};

const wedgeAntilles = 'https://swapi-api.hbtn.io/api/people/18/';
request(options, function(err, res, body) {
  let total = 0;
  const result = JSON.parse(body)

  result.results.forEach(element => {
    // console.log(element.characters)
    if (element.characters.indexOf(wedgeAntilles) > -1) {
      total++;
    }
  });
  console.log(total);
});

