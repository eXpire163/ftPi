from socketIO_client import SocketIO, LoggingNamespace
from watchdog.observers import Observer  
from watchdog.events import PatternMatchingEventHandler

class MyHandler(PatternMatchingEventHandler):
    patterns = ["*.xml", "*.lxml"]

    def process(self, event):
        """
        event.event_type 
            'modified' | 'created' | 'moved' | 'deleted'
        event.is_directory
            True | False
        event.src_path
            path/to/observed/file
        """
        # the file will be processed there
        print event.src_path, event.event_type  # print now only for degug
        socketIO.emit('start',event.event_type)

    def on_modified(self, event):
        self.process(event)

    def on_created(self, event):
        self.process(event)


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

# watch xml files for test raising events
observer = Observer()
observer.schedule(MyHandler(), path='.')
observer.start()

while True:
    socketIO.wait()
    print('wainting')
