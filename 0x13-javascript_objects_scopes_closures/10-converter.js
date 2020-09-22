#!/usr/bin/node

exports.converter = function (base) {
  return function print (number) {
    return number.toString(base);
  }
}
