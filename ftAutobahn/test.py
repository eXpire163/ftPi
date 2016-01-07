import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
port = 8
GPIO.setup(port, GPIO.IN)

def my_rising(data):
    print "rise {} {}".format(data, GPIO.input(port));




GPIO.add_event_detect(port, GPIO.BOTH, callback=my_rising, bouncetime=200)

i =0
while True:
    pass
  #print(GPIO.input(23))
  #if (GPIO.input(port)):
  #  i=i+1
  #print(i)