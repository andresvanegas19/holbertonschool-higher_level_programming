#!/usr/bin/node

const list = require('./100-data.js').list;

console.log(list)

let new_list = list.map((element, index) => {
  return element * index
})

console.log(new_list)
