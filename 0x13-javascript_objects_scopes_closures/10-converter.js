#!/usr/bin/node

function print (number, base) {
  console.log(number.toString(base))
}


exports.converter = function (base) {
  return print("", base)
}
