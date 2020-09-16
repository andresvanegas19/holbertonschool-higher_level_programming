#!/usr/bin/node

let i = 0;

process.argv.forEach(() => i++);

if (i > 2) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
