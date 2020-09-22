#!/usr/bin/env node
const { exit, cwd, argv } = require('process');
const fs = require('fs');

if (argv.length != 5) {
  exit(0)
}

const path = cwd() + '/'
const file_a = path + argv[2]
const file_b = path + argv[3]

const res_file_a = fs.readFileSync(file_a, function (err) {
    if(err) {
        return console.log(err);
    }
}).toString()
  .replace(/(\r\n|\n|\r)/gm,"");

const res_file_b = fs.readFileSync(file_b, function (err) {
    if(err) {
        return console.log(err);
    }
}).toString()
  .replace(/(\r\n|\n|\r)/gm,"");


total = res_file_a + '\n' + res_file_b + '\n'

fs.writeFile(path + argv[4], total, function (err) {
    if(err) {
        return console.log(err);
    }
});
