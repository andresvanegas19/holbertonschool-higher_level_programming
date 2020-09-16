#!/usr/bin/node

const factorial = (number) => {
  if (number === 0 || number === 1) {
    return 1;
  } else {
    return number * factorial(number - 1);
  }
};

let result;
if (isNaN(process.argv[2]) === false) {
  result = factorial(Number(process.argv[2]));
} else {
  result = 1;
}

console.log(result);
