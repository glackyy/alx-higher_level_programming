#!/usr/bin/node
let nbarg = 0;

exports.logMe = function (item) {
  console.log(nbarg + ': ' + item);
  nbarg++;
};
