import cv2
import sys
import paho.mqtt.client as mqtt
import time
import json

def printme(text):
    print("VIDEO: "+text)

client = mqtt.Client()

client.connect("localhost", 1883, 60)

#client.loop_start()

cascPath = "lib/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    printme("start loop")
    ret, frame = video_capture.read()
    printme("go gray")
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    printme("find faces")
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    printme("make json")
    facesString = json.dumps(faces)
    printme(facesString)
    client.publish("minimop/video/faces", facesString)
    printme("push")
    # Draw a rectangle around the faces
#    for (x, y, w, h) in faces:
#        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
#    cv2.imshow('Video', frame)
    time.sleep( 5 )


# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
