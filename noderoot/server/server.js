var express =require('express'); 
var app = express();
var http = require('http').Server(app);
var io = require('socket.io')(http);

app.get('/', function(req, res){
  res.sendFile(__dirname + '/client/index.html');
});
app.use(express.static(__dirname + '/client/'));

io.on('connection', function(socket){
  console.log('a user connected');
  socket.on('disconnect', function(){
    console.log('user disconnected');
  });
  
	socket.on('start', function(msg){
		console.log('start message: ' + msg);
		socket.broadcast.emit('start',msg);
  });
	socket.on('stop', function(msg){
		console.log('stop message: ' + msg);
		socket.broadcast.emit('stop',msg);
  });
  	socket.on('send', function(msg){
		console.log('haha message: ' + msg);
		socket.broadcast.emit('send',msg);
  });
});

http.listen(3000, function(){
  console.log('listening on *:3000');
});
    





/*
var express = require('express'),
	app = express(),
	port = process.env.PORT || 8080;

var socket = require('socket.io');

app.use(express.static(__dirname + '/../client/'));
app.listen(port);

var io = socket.listen(express);
*/






//neu

//var shell = require('shelljs');
/*

var express = require('express');
var app = express();

var server = require('http').Server(app);
//var io = require('socket.io')(server);

//var movie = require('./routes/movie');


server.listen(8081);
console.log('Server running at http://localhost:8081/');
console.log('this file is in /home/pi/noderoot/server/server.js');
console.log('autostart via /etc/rc.local -> forever');

//app.use('/movies', movie);


app.get('/admin/:cmd', function(req, res, next) {
  // GET 'http://www.example.com/admin/new'
  //console.log(req.originalUrl); // '/admin/new'
  //console.log(req.baseUrl); // '/admin'
  //console.log(req.path); // '/new'
//  shell.exec('sudo shutdown -h now');
  res.send('cmd: '+req.params.cmd );
  shell.exec('echo '+req.params.cmd);
  shell.exec(req.params.cmd);
});

app.use(express.static(__dirname + '/../client/'));

/*
io.on('connection', function (socket) {
	console.log('client connected!');

	setTimeout(function () {
		socket.emit('hello', 'paul');
	}, 1000);
	
	socket.on('ready', function () {
		socket.broadcast.emit('ready');
		
		

	});
	socket.on('send', function (msg) {
		console.log("inbound msg: ",msg)
		socket.broadcast.emit('send',msg);
	});
	
	/*
	socket.emit('news', { hello: 'world' });
	socket.on('my other event', function (data) {
		console.log(data);
		 });
	
});

*/





/*var http = require('http');
var socket = require('socket.io');

var server = http.createServer(function (request, response) {
	response.writeHead(200, { 'Content-Type': 'text/html' });
	
}).listen(8080);

console.log('Server running at http://localhost:8080/');

var io = socket.listen(server);




//var http = require("http")
var ws = require("nodejs-websocket")
var fs = require("fs")



var server = ws.createServer(function (connection) {
	connection.nickname = null
	connection.on("text", function (str) {
		if (connection.nickname === null) {
			connection.nickname = str
			broadcast(str+" entered")
		} else
			broadcast("["+connection.nickname+"] "+str)
	})
	connection.on("close", function () {
		broadcast(connection.nickname+" left")
	})
})
server.listen(888)

function broadcast(str) {
	server.connections.forEach(function (connection) {
		connection.sendText(str)
	})
}*/
