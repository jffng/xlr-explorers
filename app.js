var util = require('util'),
	exec = require('child_process').exec;

function get_distance(lat1, lon1, lat2, lon2){
	var arguments = lat1.toString() + ' ' + lon1.toString() + ' ' + lat2.toString() + ' ' + lon2.toString();
	exec('python LatLonConversion.py ' + arguments,
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

get_distance(40.72981741782271, -73.99342600427624, 40.72982147286832, -73.99339845073465);