# Topics



## vision

a) Post in the mqtt if there is a (known) face and where in the image

b) keep the face in diastance range 2


x) emotion detection to clone the moode


# Commands


| Use | Topic | Payload | Description |
| --- | --- | --- | --- |
| Sound | minimop/sound/tts | string | Converts string to speach and plays it |
| Sound | minimop/sound/wav | filepath | Plays the specivied output file |
| Display | minimop/display/image | filepath | Show image in oled |
| Display | minimop/display/folder | folder | folder with bmp files that all are going to be displayed from a-z |
| Display | minimop/display/drawtest | - | just a test for drawing and speedtest |
| Display | minimop/display/# | string | text to display (adds date and topic by default  |
| Motion | minimop/motion | "number,direction,speed" | number motor:1-4, direction: left\|right, speed:0.0-1.0 |

# Published infos


| Use | Topic | Payload | Description |
| --- | --- | --- | --- |
| Video | minimop/faces | {faces} | recognised faces in the webcamimage |
| Sensor | minimop/sensor/switch | data, GPIO.input(data) | publish switch changes |




# Techs

## MQTT

## Image / Face recognission

live webcam recog
https://realpython.com/blog/python/face-detection-in-python-using-a-webcam/

face finding in image 
https://realpython.com/blog/python/face-recognition-with-python/

face recog (machine lerning)
http://scikit-learn.sourceforge.net/0.6/auto_examples/applications/plot_face_recognition.html


