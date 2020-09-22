#!/usr/bin/node
const { exit, cwd, argv } = require('process');
const fs = require('fs');

if (argv.length !== 5) {
  exit(0);
}

const path = cwd() + '/';
const fileA = path + argv[2];
const fileB = path + argv[3];

const resFileA = fs.readFileSync(fileA, function (err) {
  if (err) {
    return console.log(err);
  }
}).toString()
  .replace(/(\r\n|\n|\r)/gm, '');

const resFileB = fs.readFileSync(fileB, function (err) {
  if (err) {
    return console.log(err);
  }
}).toString()
  .replace(/(\r\n|\n|\r)/gm, '');

const total = resFileA + '\n' + resFileB + '\n';

fs.writeFile(path + argv[4], total, function (err) {
  if (err) {
    return console.log(err);
  }
});
