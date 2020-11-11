var express = require('express');
var stationModel = require('../models/station');
var app = express();

app.get('/stations', async (req, res) => {
  const stations = await stationModel.find({});

  try {
    res.send(stations);
  } catch (err) {
    res.status(500).send(err);
  }
});

module.exports = app
