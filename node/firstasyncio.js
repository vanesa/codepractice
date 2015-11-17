var fs = require('fs');
var buf = fs.readFileSync(process.argv[2], function doneReading(err, fileContents) {


});
var str = buf.toString();
count = (str.match(/\n/g) || []).length;
// if (str.match(/\n/g))
// 	return true
// return false
function countNumber () {
	console.log(count);
}



// Split has to O(nxm!)

// OR: 
// var fs = require('fs')

// var contents = fs.readFileSync(process.argv[2])
// var lines = contents.toString().split('\n').length - 1
// console.log(lines)