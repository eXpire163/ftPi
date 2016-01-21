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
#
###############################################################################

from autobahn.twisted.websocket import WebSocketServerProtocol, WebSocketServerFactory
from ftMotor import FTMotor
import RPi.GPIO as GPIO

maxSpeed = 204
debug = True

class FischerServer(WebSocketServerProtocol):

    ftm = FTMotor()
    ftm.debug = debug
    print('debugmode is {}'.format(debug))
    ftm.maxSpeed = maxSpeed
    GPIO.setmode(GPIO.BOARD)
    gport = [8, 10]

    def doLog(self, txt):
        if self.debug:
            print(txt)

    def goGPIO(self, data):
        self.doLog("switch,{},{}".format(data, GPIO.input(data)))
        self.sendMessage("switch,{},{}".format(data, GPIO.input(data)))

    def onConnect(self, request):
        print request
        # create a default object, no changes to I2C address or frequency
        print("Client connecting: {0}".format(request.peer))
        for i in range(len(self.gport)):
            print(self.gport)
            print("setup: {}".format(self.gport[i]))
            GPIO.setup(self.gport[i], GPIO.IN)
            GPIO.add_event_detect(self.gport[i], GPIO.BOTH, callback=self.goGPIO, bouncetime=200)
            pass


    def onOpen(self):
        self.doLog("WebSocket connection open.")

    def onMessage(self, payload, isBinary):
        self.doLog("Text message received: {0}".format(payload.decode('utf8')))
        befehl = payload.decode('utf8').split(',')
        self.doLog(befehl)
        if(len(befehl)==4):
            print befehl
            self.ftm.setMotor(befehl[1],befehl[3],befehl[2])

        # echo back message verbatim
        if(payload != "thx"):
            self.sendMessage(payload)

    def onClose(self, wasClean, code, reason):
        self.ftm.turnOffMotors()
        for xx in range(len(self.gport)):
            try:
                self.doLog("removing")
                GPIO.remove_event_detect(self.gport[xx])
            except ValueError:
                print("cannot remove".format())

        print("WebSocket connection closed: {0}".format(reason))




if __name__ == '__main__':

    import sys

    from twisted.python import log
    from twisted.internet import reactor

    log.startLogging(sys.stdout)

    factory = WebSocketServerFactory("ws://127.0.0.1:9000", debug=True)
    factory.protocol = FischerServer

    reactor.listenTCP(9000, factory)
    reactor.run()
