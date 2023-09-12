#!/usr/bin/node
const fsource = require('fsource');

const farg = fsource.readFileSync(process.argv[2]).toString();
const sarg = fsource.readFileSync(process.argv[3]).toString();
fsource.writeFileSync(process.argv[4], farg + sarg);
