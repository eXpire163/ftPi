# deorecated start with server2

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
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import atexit
import os

maxSpeed = 203;

class MyServerProtocol(WebSocketServerProtocol):


    def onConnect(self, request):
        # create a default object, no changes to I2C address or frequency
        print("Client connecting: {0}".format(request.peer))
        #turnOffMotors();

    def onOpen(self):
        print("WebSocket connection open.")

    def onMessage(self, payload, isBinary):
        if isBinary:
            print("Binary message received: {0} bytes".format(len(payload)))
        else:
            print("Text message received: {0}".format(payload.decode('utf8')))
            befehl = payload.decode('utf8').split(',')
            print(befehl)
            if(len(befehl)==4):
                if(befehl[3]=='left'):
                    mh.getMotor(int(float(befehl[1]))).run(Adafruit_MotorHAT.FORWARD)
                else:
                    mh.getMotor(int(float(befehl[1]))).run(Adafruit_MotorHAT.BACKWARD)
                print('stopped: {0}'.format(int(float(befehl[2])*maxSpeed)))
                mh.getMotor(int(float(befehl[1]))).setSpeed(int(float(befehl[2])*maxSpeed))
            if(befehl == 'shutdown'):
                os.system("sudo halt")

        # echo back message verbatim
        self.sendMessage(payload, isBinary)

    def onClose(self, wasClean, code, reason):
        turnOffMotors()
        print("WebSocket connection closed: {0}".format(reason))


mh = Adafruit_MotorHAT(addr=0x60)
# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    print("motor aus ------------")
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

if __name__ == '__main__':

    import sys

    from twisted.python import log
    from twisted.internet import reactor

    log.startLogging(sys.stdout)

    factory = WebSocketServerFactory("ws://127.0.0.1:9000", debug=False)
    factory.protocol = MyServerProtocol
    # factory.setProtocolOptions(maxConnections=2)

    reactor.listenTCP(9000, factory)
    reactor.run()
