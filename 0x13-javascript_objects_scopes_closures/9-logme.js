#!/usr/bin/node

let timesExecution = 0;

exports.logMe = function (item) {
  console.log(`${timesExecution}: ${item}`);
  timesExecution++;
};
