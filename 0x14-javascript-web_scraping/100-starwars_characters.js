#!/usr/bin/node
const req = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
req.get(url + id, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const dt = JSON.parse(body);
  const ddir = dt.characters;
  for (const i of ddir) {
    req.get(i, function (error, response, body1) {
      if (error) {
        console.log(error);
      }
      const dt1 = JSON.parse(body1);
      console.log(dt1.name);
    });
  }
});
