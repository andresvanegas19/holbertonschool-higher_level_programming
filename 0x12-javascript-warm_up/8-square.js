#!/usr/bin/env node

if (isNaN(process.argv[2]) === false && process.argv.length > 2) {
  const total =  Number(process.argv[2])
  for (let i = 0; i < total; i++) {
    for (let j = 0; j < total; j++) {
      console.log('X');
    }
  }
} else {
  console.log('Missing number of occurrences');
}
