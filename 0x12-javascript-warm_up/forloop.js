#!/usr/bin/env node

const phrases = ['C is fun', 'Python is cool', 'Javascript is amazing'];

phrases.forEach(phrase => {
  console.log(phrase);
});

const factorial = (number) => {
  if (number === 0 || number === 1) {
    return 1;
  } else {
    return number * factorial(number - 1);
  }
};
