#!/usr/bin/node

const dict = require('./101-data.js').dict;

let new_dict = {}

for (let entry in dict) {
  if (!new_dict.hasOwnProperty(dict[entry])) {
    new_dict[dict[entry]] = []
  }
  new_dict[dict[entry]].push(entry)
}
console.log(new_dict)
