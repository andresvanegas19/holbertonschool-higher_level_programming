#!/usr/bin/env node
const { argv } = require('process');
const fs = require('fs');

const file = argv[2];

try {
  const fileResult = fs.readFileSync(file, 'utf-8');
  process.stdout.write(fileResult.toString())
} catch (err) {
  // If the type is not what you want, then just throw the error again.
  if (err.code === 'ENOENT') {
    console.log({
    'Error': 'ENOENT: no such file or directory, open \'' + file + '\'' + 'at Error (native)',
    'errno': -2,
    'code': 'ENOENT',
    'syscall': 'open',
    path: 'doesntexist' });
  } else {
    throw err;
  }

  // Handle a file-not-found error
}


