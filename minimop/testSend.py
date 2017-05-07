import paho.mqtt.client as mqtt
import json


def printme(text):
    print("VIDEO: "+text)

client = mqtt.Client()


client.connect("localhost", 1883, 60)

#client.loop_start()
faces = json.dumps( [1,2,3])
print(faces)
client.publish("minimop/faces", faces)
client.disconnect()