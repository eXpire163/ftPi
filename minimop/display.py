import paho.mqtt.client as mqtt
import os, sys, time, threading
from PIL import Image, ImageDraw, ImageFont
import Adafruit_SSD1306


def aktuelleZeit(werta, wertb):
    zeitpunktMessung = time.localtime()
    jahr, monat, tag = zeitpunktMessung[0:3]
    stunde, minute, sekunde = zeitpunktMessung[3:6]
    systemUhrzeit = str(stunde).zfill(2) + ":" + str(minute).zfill(2) + ":" + str(sekunde).zfill(2)
    systemDatum = str(tag).zfill(2) + "." + str(monat).zfill(2) + "." + str(jahr)
    if werta == "time" and wertb == "date":
        ermittelteZeit = systemUhrzeit + " " + systemDatum
    elif werta == "date" and wertb == "time":
        ermittelteZeit = systemDatum + " " + systemUhrzeit
    elif werta == "time" and wertb == "":
        ermittelteZeit = systemUhrzeit
    elif werta == "date" and wertb == "":
        ermittelteZeit = systemDatum
    else:
        ermittelteZeit = zeitpunktMessung
    return ermittelteZeit

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("minimop/display")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))



width = 128 #disp.width
height = 64 #disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
draw.rectangle((0,0,width,height), outline=0, fill=0)
padding = 2
shape_width = 20
top = padding
bottom = height-padding
x = padding
draw.text((x, top+25), 'Hello', font=font_b, fill=255)
Display image.
disp.image(image)
disp.display()

time.sleep(5)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()