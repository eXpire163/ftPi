var express = require('express');
var router = express.Router();

/* GET users listing. */
router.get('/', function (req, res) {
	res.send('respond with a resource');
	
});

/* GET users listing. */
router.get('/:id', function (req, res) {
	res.send('respond with a resource '+ req.params.id);
});


router.put('/:id', function (req, res) {
	console.log('body', req.body.user);
	res.send('putting ' + req.params.id +' -> '+ req.body.user);
});

module.exports = router;