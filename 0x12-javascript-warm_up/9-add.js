#!/usr/bin/env node
function add (a, b) {
  return a + b;
}

if (isNaN(process.argv[2]) === false && process.argv.length > 2 &&
    isNaN(process.argv[3]) === false) {
  console.log(add(Number(process.argv[2]), Number(process.argv[3])));
} else {
  console.log('NaN');
}
