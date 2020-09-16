#!/usr/bin/node

if (isNaN(process.argv[2]) === false && process.argv.length > 2) {
  for (let i = 0; i < Number(process.argv[2]); i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
