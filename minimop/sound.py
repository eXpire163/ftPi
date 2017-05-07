import paho.mqtt.client as mqtt
import pygame
from gtts import gTTS
from tempfile import TemporaryFile


def printme(text)
    print("SOUND: "+text)
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    printme("Connected with result code "+str(rc))
    client.subscribe("minimop/sound")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    printme(msg.topic+" "+str(msg.payload))
    if(msg.topic=="tts"):
        tts = gTTS(text=msg.payload, lang='en')
        f = TemporaryFile()
        tts.write_to_fp(f)
        printme("Created tempfile")
        pygame.mixer.music.load(f.name)
        printme("play sound")
        pygame.mixer.music.play()
        printme("close temp")
        f.close()
    elif (msg.topic =="wav"):

        if(os.path.isfile("fx/"+msg.payload)): 
            pygame.mixer.music.load("fx/"+msg.payload)
            pygame.mixer.music.play()
    else:
        if(os.path.isfile("fx/SciFiRobotSound.wav"):
            pygame.mixer.music.load("fx/SciFiRobotSound.wav")
            pygame.mixer.music.play()

    


pygame.mixer.init()

#while pygame.mixer.music.get_busy() == True:
#    continue

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()