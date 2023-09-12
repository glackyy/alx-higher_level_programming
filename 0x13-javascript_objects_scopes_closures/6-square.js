#!/usr/bin/node
const SquareX = require('./5-square');

class Square extends SquareX {
  charPrint (ch) {
    if (ch === undefined) {
      ch = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let s = '';
      for (let j = 0; j < this.width; j++) {
        s += ch;
      }
      console.log(s);
    }
  }
}

module.exports = Square;
