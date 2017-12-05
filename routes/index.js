var express = require('express');
var router = express.Router();
var spawn = require('child_process').spawn

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.get('/test', function(req, res, next) {
  res.render('testindex', { title: 'Express' });
});

router.get('/:text', function(req, res, next) {
	// python calling
	py    = spawn('python', ['compute_input.py']),
    data = [1,2,3,4,5,6,7,8,9],
    dataString = '';
	py.stdout.on('data', function(data){
	  dataString += data.toString();
	});
	py.stdout.on('end', function(){
	  console.log('Sum of numbers=',dataString);
	});
	py.stdin.write(JSON.stringify(data));
	py.stdin.end();
	// end of python call code

  res.render('index', { title: 'Express' });
});
module.exports = router;
