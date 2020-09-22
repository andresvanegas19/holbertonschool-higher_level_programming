#!/usr/bin/node
const { argv } = require('process');
const fs = require('fs');

const file = argv[2];
fs.readFile(file, 'utf-8', function (error, data) {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
