import time
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO


def printme(text):
    print("SENSOR: "+text)

def on_gpio(data):
    printme("switch,{},{}".format(data, GPIO.input(data)))
    client.publish("minimop/sensor/switch", "{},{}".format(data, GPIO.input(data)))



def on_connect():
    print "## Activating GPIO Events ##"
    for i in range(len(gport)):
        printme("setup: {}".format(gport[i]))
        GPIO.setup(gport[i], GPIO.IN)
        GPIO.add_event_detect(gport[i], GPIO.BOTH, callback=on_gpio, bouncetime=200)

def on_disconnect():
    print "## Deactivating GPIO Events ##"
    for port_id in range(len(gport)):
        try:
            printme("removing")
            GPIO.remove_event_detect(gport[port_id])
        except ValueError:
            printme("cannot remove".format())





if __name__ == '__main__':
    try:
        client = mqtt.Client()
        client.connect("localhost", 1883, 60)

        # Connect GPIO
        printme("Preparing to GPIO")
        GPIO.setmode(GPIO.BOARD)
        gport = [8, 10]


        while True:
            time.sleep(1)  # 1s
    except KeyboardInterrupt:
        print("Bye!")
