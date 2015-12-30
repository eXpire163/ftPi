
var express = require('express');
var router = express.Router();

/* GET users listing. */
router.get('/', function (req, res) {
	
	
	
	var mysql = require('mysql');
	var connection = mysql.createConnection({
		host     : 'localhost',
		user     : 'root',
		password : '',
	database: 'proficrawler'
	});
	
	connection.connect();
	
	connection.query('SELECT * from website', function (err, rows, fields) {
		if (err) throw err;
		
		console.log('The solution is: ', rows.length);
		res.send(rows);
	});
	
	connection.end();
	

	
	
});

/* GET users listing. */
router.get('/:id', function (req, res) {
	res.send('respond with a resource ' + req.params.id);
});


router.put('/:id', function (req, res) {
	console.log('body', req.body.user);
	res.send('putting ' + req.params.id + ' -> ' + req.body.user);
});

module.exports = router;


