#!/usr/bin/node

let times_execution = 0;

exports.logMe = function (item) {
  console.log(`${times_execution}: ${item}`)
  times_execution++;
}
