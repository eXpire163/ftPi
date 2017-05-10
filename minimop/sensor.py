import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import atexit
import time

def printme(text):
    print("SENSOR: "+text)
	
def on_gpio(data):
    printme("switch,{},{}".format(data, GPIO.input(data)))
	client.publish("minimop/sensor/switch", "{},{}".format(data, GPIO.input(data))

	
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

	
	
client = mqtt.Client()

client.connect("localhost", 1883, 60)



atexit.register(turnOffDisp)

# Connect GPIO
printme "Preparing to GPIO"
GPIO.setmode(GPIO.BOARD)
gport = [8, 10]

try:
    while True:
        time.sleep(1)  # 1s
except KeyboardInterrupt:
    print("Bye!")
    
