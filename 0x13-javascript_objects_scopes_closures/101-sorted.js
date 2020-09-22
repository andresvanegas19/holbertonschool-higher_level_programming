#!/usr/bin/node

const dict = require('./101-data.js').dict;

const newDict = {};

for (const entry in dict) {
  if (!newDict.hasOwnProperty.call(dict[entry])) {
    newDict[dict[entry]] = [];
  }
  newDict[dict[entry]].push(entry);
}

console.log(newDict);
