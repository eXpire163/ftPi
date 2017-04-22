import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
port = [8,10]

#port = map(int, port)

def my_rising(data):
    print "rise {} {}".format(data, GPIO.input(data))

print port

# setup events
#for xx in port:



for xx in range(len(port)):
    print(xx,port[xx])
    print("setup: ".format(int(xx)))
    GPIO.setup(port[xx], GPIO.IN)
    GPIO.add_event_detect(port[xx], GPIO.BOTH, callback=my_rising, bouncetime=200)


# remove events

i =0
while True:
    pass
  #print(GPIO.input(23))
  #if (GPIO.input(port)):
  #  i=i+1
  #print(i)