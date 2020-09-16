#!/usr/bin/node

if (isNaN(process.argv[2]) === false && process.argv.length > 2) {
  const total = Number(process.argv[2]);
  for (let i = 0; i < total; i++) {
    for (let j = 0; j < total; j++) {
      process.stdout.write('X');
    }
    console.log();
  }
} else {
  console.log('Missing number of occurrences');
}
