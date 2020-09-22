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

const wedgeAntilles = 'https://swapi-api.hbtn.io/api/people/18/';
request(options, function (err, res, body) {
  if (err) throw err;

  let total = 0;
  const result = JSON.parse(body);

  result.results.forEach(element => {
    if (element.characters.indexOf(wedgeAntilles) > -1) {
      total++;
    }
  });
  console.log(total);
});
