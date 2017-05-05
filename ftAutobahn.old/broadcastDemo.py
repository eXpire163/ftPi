###############################################################################
#
# The MIT License (MIT)
#
# Copyright (c) Tavendo GmbH
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
# https://github.com/crossbario/autobahn-python/tree/master/examples/twisted/websocket/broadcast
###############################################################################

import sys

from twisted.internet import reactor
from twisted.python import log
from twisted.web.server import Site
from twisted.web.static import File

from autobahn.twisted.websocket import WebSocketServerFactory, \
    WebSocketServerProtocol, \
    listenWS
#import RPi.GPIO as GPIO

class BroadcastServerProtocol(WebSocketServerProtocol):

    def onOpen(self):
        self.factory.register(self)

    def onMessage(self, payload, isBinary):
        if not isBinary:
            msg = "{} from {}".format(payload.decode('utf8'), self.peer)
            if payload != "thx":
                self.factory.broadcast(msg)
            
    def connectionLost(self, reason):
        WebSocketServerProtocol.connectionLost(self, reason)
        self.factory.unregister(self)


class BroadcastServerFactory(WebSocketServerFactory):

    """
    Simple broadcast server broadcasting any message it receives to all
    currently connected clients.
    """

    #def goGPIO(self, data):
    #    #self.doLog("switch,{},{}".format(data, GPIO.input(data)))
    #    self.broadcast("switch,{},{}".format(data, GPIO.input(data)))

    def onKeyPress(self, event):
        print('You pressed %s\n' % (event.char, ))
        self.broadcast('You pressed %s\n' % (event.char, ))
    
    def __init__(self, url, debug=False, debugCodePaths=False):
        WebSocketServerFactory.__init__(self, url, debug=debug, debugCodePaths=debugCodePaths)
        self.clients = []
        self.tickcount = 0
        self.tick()

    def tick(self):
        self.tickcount += 1
        self.broadcast("tick %d from server" % self.tickcount)
        reactor.callLater(1, self.tick)

    def register(self, client):
        if client not in self.clients:
            print("registered client {}".format(client.peer))
            #GPIO.setup(8, GPIO.IN)
            print("setup port 8")
            #GPIO.add_event_detect(8, GPIO.BOTH, callback=self.goGPIO, bouncetime=200)
            print("activate port 8")
            self.clients.append(client)
            self.bind('<KeyPress>', self.onKeyPress)
            print("add done")

    def unregister(self, client):
        if client in self.clients:
            print("unregistered client {}".format(client.peer))
            self.clients.remove(client)

    def broadcast(self, msg):
        print("broadcasting message '{}' .. to {} clients".format(msg, len(self.clients)))
        for c in self.clients:
            c.sendMessage(msg.encode('utf8'))
            print("message sent to {}".format(c.peer))


class BroadcastPreparedServerFactory(BroadcastServerFactory):

    """
    Functionally same as above, but optimized broadcast using
    prepareMessage and sendPreparedMessage.
    """

    def broadcast(self, msg):
        print("broadcasting prepared message '{}' ..".format(msg))
        preparedMsg = self.prepareMessage(msg)
        for c in self.clients:
            c.sendPreparedMessage(preparedMsg)
            print("prepared message sent to {}".format(c.peer))


if __name__ == '__main__':

    if len(sys.argv) > 1 and sys.argv[1] == 'debug':
        log.startLogging(sys.stdout)
        debug = True
    else:
        debug = False

    #GPIO.setmode(GPIO.BOARD)
    ServerFactory = BroadcastServerFactory
    # ServerFactory = BroadcastPreparedServerFactory

    factory = ServerFactory(u"ws://127.0.0.1:9000",
                            debug=debug,
                            debugCodePaths=debug)

    factory.protocol = BroadcastServerProtocol
    listenWS(factory)

    webdir = File('../noderoot/client/')
    web = Site(webdir)
    reactor.listenTCP(9001, web)

    reactor.run()