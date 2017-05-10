import paho.mqtt.client as mqtt
import os, sys, time, threading, datetime
from PIL import Image, ImageDraw, ImageFont
import Adafruit_SSD1306
import atexit



def printme(text):
    print("DISPLAY: "+text)

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

def updateText(topic, payload):
    draw.rectangle((0,0,width,height), outline=0, fill=0) #Display leeren
    displayTime = aktuelleZeit("time", "date") # bei Abfrage "date","time" aendert die Reihenfolge der Ausgabe
    draw.text((x, top), topic , font=font, fill=255)
    draw.text((x, top+20), payload, font=font_c, fill=255)
    draw.line((x, top+45, x+width, top+45), fill=255)
    draw.text((x, top+50), displayTime, font=font, fill=255)
    #image.show()
    disp.image(image)
    disp.display()

def updateImage(imagepath):
    image = Image.open(imagepath)
    #image_r = image.resize((width,height), Image.BICUBIC)
    #image_bw = image_r.convert("1")
 
    # Finally this bit maps each pixel (depending on whether it is black or white) to the display.
    # Note here we are not using the text command like in previous programs. We use led.draw_pixel:
    # That way we can individually address each pixel and tell it to be either on or off (on = white, off = black)
 
    #for x in range(width):
    #    for y in range(height):
    #            disp.draw_pixel(x,y,bool(int(image_bw.getpixel((x,y)))))
    if(image.mode != "1"):
        image2 = image.convert("1")
        image2.save(imagepath, "BMP")
        printme("Converted and saved "+imagepath)
        disp.image(image2)
    else:
        disp.image(image)

    
    disp.display()


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    printme("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("minimop/display/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    printme(msg.topic+" "+str(msg.payload))
    if(msg.topic=="minimop/display/image"):
        printme("slide");
        updateImage(msg.payload)
    elif(msg.topic=="minimop/display/folder"):
        filelist = os.listdir(msg.payload)
        filelist.sort()
        for file in filelist:
            if file.endswith(".bmp"):
                printme(os.path.join("file: ", file))
                updateImage(os.path.join(msg.payload,file))
                #time.sleep(0.025)
    elif(msg.topic=="minimop/display/drawtest"):
        totaltime=datetime.datetime.now()-datetime.datetime.now();
        for x in range(width-3):
            a = datetime.datetime.now()
            image = Image.new('1', (width, height))
            draw = ImageDraw.Draw(image)
            draw.line((x , 0) + (x, height-1), fill=80)
            draw.line((x+1 , 0) + (x, height-1), fill=160)
            draw.line((x+2 , 0) + (x, height-1), fill=255)
            
            b = datetime.datetime.now()
            disp.image(image)
            c = datetime.datetime.now()
            disp.display()
            d = datetime.datetime.now()
            printme("ba {} cb {} dc {} total {}".format(b-a,c-b,d-c, d-a))
            totaltime+=(d-a)
        printme("total time = {}".format(totaltime))
        
    else:
        printme("no slide, "+msg.topic)
        updateText(msg.topic, msg.payload)

def turnOffDisp():
    disp.clear()
    disp.display()

def showSplash():
    printme("Display splash screen")
    image = Image.new('1', (width, height))
    draw = ImageDraw.Draw(image)
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    padding = 2
    shape_width = 20
    top = padding
    bottom = height-padding
    x = padding
    draw.text((x, top+25), 'Hello', font=font_b, fill=255)
    disp.image(image)
    disp.display()
    time.sleep(2)

    


# Raspberry Pi pin configuration:
RST = 24
 
# Display 128x64 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
 
# Initialize library.
disp.begin()
 
# Clear display.
disp.clear()
disp.display()

atexit.register(turnOffDisp)

width = disp.width
height = disp.height
# font = ImageFont.load_default() # Wenn keine eigene Schrift vorhanden ist!!!! 
font = ImageFont.truetype("fonts/VERDANAB.TTF", 12) # Schriftart, Schriftgroesse
font_b = ImageFont.truetype("fonts/VERDANAB.TTF", 18)
font_c = ImageFont.truetype("fonts/VERDANAB.TTF", 14)

showSplash()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
