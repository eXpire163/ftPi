from socketIO_client import SocketIO, LoggingNamespace

def on_connect():
    print('connect')

def on_disconnect():
    print('disconnect')

def on_reconnect():
    print('reconnect')

def on_start(*args):
    print('start', args)

def on_stop(*args):
    print('stop', args)

socketIO = SocketIO('localhost', 3000, LoggingNamespace)
socketIO.on('connect', on_connect)
socketIO.on('disconnect', on_disconnect)
socketIO.on('reconnect', on_reconnect)

# Listen
socketIO.on('start', on_start)
socketIO.on('stop', on_stop)

while True:
    socketIO.wait()
    print('wainting')