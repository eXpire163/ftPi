from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import atexit

class FTShield:
    maxSpeed = 204
    dir = {}
    spe = {}
    mh = ""
    debug = True
    isLive = True

    def __init__(self):
        atexit.register(self.turnOffMotors)
        self.mh = Adafruit_MotorHAT(addr=0x60)

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
            if isLive:
                self.mh.getMotor(nummer).setSpeed(0)
            
            if direction == 'left':
                if isLive: 
                    self.mh.getMotor(nummer).run(Adafruit_MotorHAT.FORWARD)
            else:
                if isLive:
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
        self.log('set {} {} {}'.format(nummer, direction, speed))
        num = int(float(nummer))
        dir = direction
        tempo = int(float(speed)*self.maxSpeed)
        self.setDirection(num, direction)
        self.setSpeed(num, tempo)
        pass

    def turnOffMotors(self):
        print("motor aus ------------")
        self.mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
        self.mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
        self.mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
        self.mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
