#!/usr/bin/env nodejs
const { argv } = require('process');
const fs = require('fs');

const fileA = argv[2];
const fileB = argv[3];

const resFileA = fs.readFileSync(fileA, function (err) {
  if (err) {
    return console.log(err);
  }
});

const resFileB = fs.readFileSync(fileB, function (err) {
  if (err) {
    return console.log(err);
  }
});

const total = resFileA + resFileB;

console.log(total)

fs.writeFile(argv[4], total, function (err) {
  if (err) {
    return console.log(err);
  }
});
