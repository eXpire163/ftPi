//define a global application
angular.module('App', ['Services']);

//create an app router for url management and redirect
angular.module('App').config(function ($routeProvider) {
	$routeProvider.when('/frontpage', {
		templateUrl: 'partials/frontpage.html',
		controller: 'frontpage',
	});
	$routeProvider.otherwise({ redirectTo: '/frontpage' });
});

//frontpage controller
angular.module('App').controller('frontpage', function ($scope, Socket) {
	console.log('Hello from the Frontpage Controller');
	$scope.name = 'Paul';
	
	
	//socket

	$scope.loading = true;
	$scope.readys = [];
	
	Socket.on('hello', function (name) {
		$scope.name = name;
		$scope.loading = false;
	});
	
	Socket.on('ready', function () {
		$scope.readys.push('Ready Event!');
	});
	
	Socket.on('send', function (msg) {
		$scope.readys.push(msg);
	});
	
	$scope.setReady = function () {
		Socket.emit('ready');
		$scope.readys.push('I AM READY!');
	};

	$scope.submit = function () {
		Socket.emit('send', $scope.name+":"+$scope.msg);
		$scope.readys.push("ich: "+$scope.msg);
	};  



});


angular.module('Services', []).
    factory('Socket', function ($rootScope) {
	var socket = io.connect();
	return {
		on: function (eventName, callback) {
			socket.on(eventName, function () {
				var args = arguments;
				$rootScope.$apply(function () {
					callback.apply(socket, args);
				});
			});
		},
		emit: function (eventName, data, callback) {
			if (typeof data == 'function') {
				callback = data;
				data = {};
			}
			socket.emit(eventName, data, function () {
				var args = arguments;
				$rootScope.$apply(function () {
					if (callback) {
						callback.apply(socket, args);
					}
				});
			});
		},
		emitAndListen: function (eventName, data, callback) {
			this.emit(eventName, data, callback);
			this.on(eventName, callback);
		}
	};
});