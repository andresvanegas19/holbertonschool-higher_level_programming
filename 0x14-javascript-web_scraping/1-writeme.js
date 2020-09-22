#!/usr/bin/env node
const fs = require('fs');
const { argv } = require('process');

const file = argv[2];
const text = argv[3];


fs.writeFile(file, text, function (err) {
  if (err) {
    return console.log(err);
  }
});
