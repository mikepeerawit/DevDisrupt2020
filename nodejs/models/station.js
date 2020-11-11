// Define schema
var mongoose = require("mongoose");

var StationSchema = new mongoose.Schema({
  name: String,
  population: Number,
  crowd: String
});

// Export model
var Station = mongoose.model("Station", StationSchema);
module.exports = Station;
