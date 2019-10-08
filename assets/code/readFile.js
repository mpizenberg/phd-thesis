let fs = require('fs');
fs.readFile('file.txt', 'utf8', function(err, contents) {
	console.log(contents);
});
