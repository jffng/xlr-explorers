var express = require('express');
var app = express();
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

var server = app.listen(3000, function () {

  var host = server.address().address;
  var port = server.address().port;

  console.log('Example app listening at http://%s:%s', host, port);

});

app.post('/radio1/data', function(req, res){
	var data = req.body;
	console.log("radio1: " );
	console.log(data);
		res.end();
});

app.post('/radio2/data', function(req, res){
	var data = req.body;
	console.log("radio2: " );
	console.log(data);
	res.end();
});

app.post('/radio3/data', function(req, res){
	var data = req.body;
	console.log("radio3: " );
	console.log(data);
	res.end();
});








