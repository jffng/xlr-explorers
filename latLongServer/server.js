var express = require('express');
var app = express();
var util = require('util'),
	exec = require('child_process').exec;

var bodyParser     =        require("body-parser");
//Here we are configuring express to use body-parser as middle-ware.
app.use(bodyParser.urlencoded({ extended: false }));
// app.use(express.static(__dirname + '/public'));


app.get('/radio1', function (req, res) {
 res.sendFile(__dirname + '/radio1.html');
});
app.get('/radio2', function (req, res) {
 res.sendFile(__dirname + '/radio2.html');
});
app.get('/radio3', function (req, res) {
 res.sendFile(__dirname + '/radio3.html');
});

app.get('/data', function (req, res) {
	var allLocations = {
		radio1:radio1, radio2:radio2, radio3:radio3
	};
	
	 res.send( res.send(JSON.stringify(allLocations)));
	  res.end();
});


var server = app.listen(3000, function () {

  var host = server.address().address;
  var port = server.address().port;

  console.log('Example app listening at http://%s:%s', host, port);

});

var radio1 = {
	lat: '40.7297915',
	lon: '-73.9935505'
}
var radio2 = {
	lat: '40.7297915',
	lon: '-73.9935505'
}
var radio3 = {
	lat: '40.7297915',
	lon: '-73.9935505'
}

app.post('/radio1/data', function(req, res){
	var data = req.body;
	console.log("radio1: " );
	console.log(data);
	radio1.lat = data.lat;
	radio1.lon = data.long;
	res.end();
});

app.post('/radio2/data', function(req, res){
	var data = req.body;
	console.log("radio2: " );
	console.log(data);
	radio2.lat = data.lat;
	radio2.lon = data.long;
	res.end();
});

app.post('/radio3/data', function(req, res){
	var data = req.body;
	console.log("radio3: " );
	console.log(data);
	radio3.lat = data.lat;
	radio3.lon = data.long;
	res.end();
});




function get_distance(lat1, lon1, lat2, lon2, lat3, lon3){

	var arguments = "-radio1 "+ lat1.toString() + ' ' + lon1.toString() + ' ' + "-radio2 " + lat2.toString() + ' ' + lon2.toString()+ ' ' + "-radio3 "  + lat3.toString() + ' ' + lon3.toString();;
	console.log(arguments);
	exec('python ../trigV2.py ' + arguments,
		function (error, stdout, stderr) {
			console.log('stdout: ' + stdout);
			console.log('stderr: ' + stderr);
			if (error !== null) {
				console.log('exec error: ' + error);
			}else{
				console.log('done');
			}
	});
}

setInterval(function(){
	get_distance(radio1.lat, radio1.lon, radio2.lat, radio2.lon, radio3.lat, radio3.lon);

},10000);







