﻿from autobahn.twisted.websocket import WebSocketServerProtocol, WebSocketServerFactory
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import atexit

class FTMotor:
    maxSpeed = 204
    dir = {}
    spe = {}
    mh = Adafruit_MotorHAT(addr=0x60)
    debug = False

    def __init__(self):
        atexit.register(self.turnOffMotors)

    def log(self,txt):
        if self.debug:
            print(txt)

    def getDirection(self, nummer):
        try:
            return self.dir[nummer]
        except KeyError:
            return 'nix'

    def setDirection(self, nummer, direction):
        if self.getDirection(nummer) != direction:
            self.setSpeed(nummer,0.0)
            self.dir[nummer] = direction
            self.log('set {} {}'.format(nummer, direction))
            self.mh.getMotor(nummer).setSpeed(0)
            if direction == 'left':
                self.mh.getMotor(nummer).run(Adafruit_MotorHAT.FORWARD)
            else:
                self.mh.getMotor(nummer).run(Adafruit_MotorHAT.BACKWARD)

        else:
            self.log('skip set {} {}'.format(nummer, direction))

    def getSpeed(self, nummer):
        try:
            return self.spe[nummer]
        except KeyError:
            return 0

    def setSpeed(self, nummer, tempo):
        if self.getSpeed(nummer) != tempo:
            self.spe[nummer] = tempo
            self.log('set {} {}'.format(nummer, tempo))
        else:
            self.log('skip set {} {}'.format(nummer, tempo))

    def setMotor(self, nummer, direction, speed):
        num = int(float(nummer))
        dir = direction
        tempo = int(float(speed)*self.maxSpeed)
        self.setDirection(nummer,direction)
        self.setSpeed(nummer, speed)
        print('set {} {} {}'.format(nummer, direction, tempo))
        pass

    def turnOffMotors(self):
        print("motor aus ------------")
        self.mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
        self.mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
        self.mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
        self.mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)


#ftm = FTMotor()
#ftm.setSpeed(1 , 2.0)
#ftm.setSpeed(1 , 2.0)
#ftm.setDirection(1, 'left')
#ftm.setMotor(3,'right',1.0)
#ftm.setMotor(3,'left',1.0)
#print ftm.getDirection(1)
#print ftm.getDirection(2)
#print ftm.getSpeed(1)
#print ftm.getSpeed(2)


