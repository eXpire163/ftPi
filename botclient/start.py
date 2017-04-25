from socketIO_client import SocketIO, LoggingNamespace
from ftShield import FTShield
import RPi.GPIO as GPIO


def doLog(self, txt):
    if self.debug:
        print(txt)



def on_gpio(self, data):
    print("switch,{},{}".format(data, GPIO.input(data)))
    sendMessage("switch,{},{}".format(data, GPIO.input(data)))


def on_connect():
    print "## Activating GPIO Events ##"
    for i in range(len(gport)):
        doLog("setup: {}".format(gport[i]))
        GPIO.setup(gport[i], GPIO.IN)
        GPIO.add_event_detect(gport[i], GPIO.BOTH, callback=on_gpio, bouncetime=200)
        pass

def on_disconnect():
    print "## Deactivating GPIO Events ##"
    ftshield.turnOffMotors()
    for xx in range(len(gport)):
        try:
            doLog("removing")
            GPIO.remove_event_detect(gport[xx])
        except ValueError:
            doLog("cannot remove".format())

def on_reconnect():
    print('reconnect')

def on_start(*args):
    doLog('start', args)
    befehl = payload.decode('utf8').split(',')
    if(len(befehl)==3):
        ftshield.setMotor(befehl[0],befehl[2],befehl[1])

print "**********************************************"
print "*********** Starting Bot Brain ***************"
print "**********************************************"

print "## Connecting to Server ##"
socketIO = SocketIO('localhost', 3000, LoggingNamespace)
socketIO.on('connect', on_connect)
socketIO.on('disconnect', on_disconnect)
#socketIO.on('reconnect', on_reconnect)

# Listen
socketIO.on('start', on_start)
#socketIO.on('stop', on_stop)

# Connect device

print "## Connecting to Shield ##"
maxSpeed = 204
debug = True
ftshield = FTShield()
ftshield.debug = debug
print('debugmode is {}'.format(debug))
ftshield.maxSpeed = maxSpeed

# Connect GPIO
print "## Preparing to GPIO ##"
GPIO.setmode(GPIO.BOARD)
gport = [8, 10]



while True:
    socketIO.wait()
    print('wainting')