#!/usr/bin/node

const Rectangle = require('./4-rectangle.js');

module.exports = class Square extends Square5 {
  constructor (size) {
    super(size, size);
    this.size = size;
  }
};
