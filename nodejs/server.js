var express = require('express');
var mongoose = require("mongoose");
var stationRouter = require('./routes/stationRoutes.js')

var app = express();
app.use(express.json());
// Set up mongoose module

mongoose.connect("mongodb+srv://usertest:VTAFqNqnUk5nF8EL@cluster0.jodck.mongodb.net/Station?retryWrites=true&w=majority", { useUnifiedTopology: true, useNewUrlParser: true });

app.use(stationRouter);

app.listen(30000, () => { console.log('Server is running...')});
