# ftPi

This is yet a preannouncement of my fischertechnik raspberry mix project. Have a look at the [wiki](https://github.com/eXpire163/ftPi/wiki/usage).

## the idea

Cheap and easy to use alternativ to the expensive fischertechnik txt controller.

## what we want
### Hardware

- Controlling motors (at least 4, maybe more)
- reading switches (digital read, at least 4)
- reading sensors (analog read)

### Software

- flowbased Development ( Known from fischertechnik software)
- webbased controlling (eg: like rc remote , or Smartphone gyro)
- fpv mode (Support for on Board Webcam with live stream)

## Used Components

### Hardware

- Raspberry Pi 1 (can be newer) (Raspberry Zero @ 5$ will probably work, but without fpv/webcam)
- Arduino Motor and Stepper Head (can be stacked for more motors - 4 DC or 2 Stepper) [link](https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi/overview)
- (upcomming) Arduino Servo Head (supports up to 16 servos) [link](https://learn.adafruit.com/adafruit-16-channel-pwm-servo-hat-for-raspberry-pi/overview)

Optional

- USB Powerbank - for mobile Raspberry power supply
- 7.4 V Lipo - for motor power (you can use the powerbank instread, but that makes it a bit weak - fischertechnik requires 6/9 V for the motors)

### Software

- Raspbean Wheezy (newer not tested yet)
- NodeJS as FrontEnd Server - eXpress
- NodejS as Backend Server - socketIO
- ShieldControl with Python triggered by ws
- Websocket communication 
- [GoJS](http://gojs.net/latest/samples/flowchart.html) for Programming UI
- mjpg_streamer for webcam access

# Status: 

- I've got the first working edition (for developer or linux gurus only) XD
![alt tag](http://hellofheaven.org/_staticImages/ftpi_preview.JPG)


# TODOs:

- Upload the code - Working on V2
- pray for ne licence / patent problems
- write a guide
- link all stuff
- clean the code
- publish in ft community
- learn how to publish on github correctly ;)
- find someone fixing my typos

and mutch more

testcommit
