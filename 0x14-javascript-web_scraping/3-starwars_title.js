#!/usr/bin/node
const req = require('request');
const epnum = process.argv[2];
const API_URL = 'https://swapi-api.hbtn.io/api/films/';
req(API_URL + epnum, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const respJSON = JSON.parse(body);
    console.log(respJSON.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
