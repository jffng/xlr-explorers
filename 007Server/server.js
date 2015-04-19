var express = require('express');
var app = express();
var util = require('util'),
	exec = require('child_process').exec;
var PythonShell = require('python-shell');

var bodyParser     =        require("body-parser");
//Here we are configuring express to use body-parser as middle-ware.
app.use(bodyParser.urlencoded({ extended: false }));
// app.use(express.static(__dirname + '/public'));



app.get('/', function (req, res) {
 res.sendFile(__dirname + '/index.html');
});

var location = {
	lat:40.732116,
	lng:-73.998630
}

app.get('/data', function (req, res) {
	 res.send( JSON.stringify(location));
	 res.end();
});

app.post('/sendData', function (req, res) {
	 // req.body 
	 console.log(req.body)
	 location.lat = req.body.point[0]
	 location.lng = req.body.point[1]
	 // res.send( JSON.stringify(location));
	 res.end();
});

var server = app.listen(3000, function () {

  var host = server.address().address;
  var port = server.address().port;

  console.log('Example app listening at http://%s:%s', host, port);

});


 
var options = {
  mode: 'json', 
  args: ['-radio1','40.7297213', '-73.9935996','-radio2' , '40.7295901' ,'-73.9937835', '-radio3' , '40.7297844', '-73.9933162' ]
  // args: ['-radio1', '40.732116' ,'-73.998630' ,'-radio2' , '40.730820' , '-73.997455' , '-radio3' , '40.731190' , '-73.997111' ]
};
 
PythonShell.run('trigV2.py', options, function (err, results) {
  if (err) throw err;
  // results is an array consisting of messages collected during execution 
  // [{"point":[40.72937967823231,-73.99328311000485]}]
  console.log('results: %j', results);
  // location.lat = results[0].point[0];
  // location.lng = results[0].point[1];
});
