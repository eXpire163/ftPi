var socket = null;
var isopen = false;
var ip = window.location.hostname;


window.onload = function () {
	socket = new io("ws://"+ip+":3000");
	socket.binaryType = "arraybuffer";
	socket.onopen = function () {
		add("Connected!");
		isopen = true;
	}
	socket.on("start", function (msg, rinfo) {
		add("Packet recieved from server: " + msg);
	});
	socket.onmessage = function (e) {
		add("checkincome: "+e +" "+e.data)
		if (typeof e.data == "string") {
			add("in: " + e.data);
		} else {
			var arr = new Uint8Array(e.data);
			var hex = '';
			for (var i = 0; i < arr.length; i++) {
				hex += ('00' + arr[i].toString(16)).substr(-2);
			}
			add("Binary message received: " + hex);
		}
		//socket.send("thx");
	}
	socket.onclose = function (e) {
		add("Connection closed.");
		socket = null;
		isopen = false;
	}
};

function add(text) {
	var TheTextBox = document.getElementById("tx");
	TheTextBox.value = TheTextBox.value + "\r\n" + text;
	TheTextBox.scrollTop = TheTextBox.scrollHeight;
	console.log(text);
}


function start(motorNumber, direction, speed) {
    if (speed == undefined) {
        speed = 1.0;
    }
    add("start motor "+motorNumber);
    socket.emit("start",  motorNumber + ","+speed+"," + direction);
};
//stop
function stop(motorNumber, direction) {
	add("stop motor");
	socket.emit("start",  motorNumber + ",0.0," + direction);
};

