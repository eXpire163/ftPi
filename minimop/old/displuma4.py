import sys
import random

import time

#from demo_opts import get_device

import luma.core.render
from luma.core.sprite_system import framerate_regulator

try:
    from luma.core.interface.serial import i2c, spi
    from luma.oled.device import ssd1306
    testenv = False
except ImportError:
    testenv = True
    



class Eyes(object):
    def __init__(self):
        self.resetVars()
        self._starttime = 0
        self._duration = 0
        self._actionstep = 0
        self._action = "non"

    def resetVars(self):
        self._x = 64
        self._y = 20
        self._space = 5
        self._color = "white"

        self._w_left = 24
        self._h_left = 24
        self._x_left = self._x - self._w_left - self._space
        self._y_left = self._y

        self._w_right = 24
        self._h_right = 24
        self._x_right = self._x + self._space
        self._y_right = self._y

    def setAction(self, action, duration):
        self.resetVars()
        self._action = action
        self._duration = duration
        self._starttime = time.time()
        self._actionstep = 0
    

    def update_pos(self):
        print(self._action)
        if(self._action=="zwinkern"):
            if(self._actionstep == 0):
                self._h_left-=1
                if(self._h_left < 8):
                    self._actionstep =1
            elif(self._actionstep == 1):
                self._h_left+=2
                if(self._h_left >= 24):
                    self._actionstep = 2
            else:
                self._action = ""
            

    def draw(self, canvas):
        #left
        canvas.rectangle((self._x_left, self._y_left, self._x_left + self._w_left, self._y_left + self._h_left), fill=self._color)
        #right
        canvas.rectangle((self._x_right, self._y_right, self._x_right + self._w_right, self._y_left + self._w_left), fill=self._color)



def main(num_iterations=sys.maxsize):
    #colors = ["red", "orange", "yellow", "green", "blue", "magenta"]
    eyes = Eyes()

    eyes.setAction("zwinkern", 1.0)

    frame_count = 0
    fps = ""
    canvas = luma.core.render.canvas(device)

    regulator = framerate_regulator(fps=0)

    while num_iterations > 0:
        with regulator:
            num_iterations -= 1

            frame_count += 1
            with canvas as c:
                #c.rectangle(device.bounding_box, outline="white", fill="black")
                eyes.update_pos()
                eyes.draw(c)
                c.text((2, 0), fps, fill="white")

            if frame_count % 20 == 0:
                fps = "FPS: {0:0.3f}".format(regulator.effective_FPS())


if __name__ == '__main__':
    try:

        if(not testenv):
            # rev.1 users set port=0
            # substitute spi(device=0, port=0) below if using that interface
            serial = i2c(port=1, address=0x3C)
            # substitute ssd1331(...) or sh1106(...) below if using that device
            device = ssd1306(serial)
        
        
        main()
    except KeyboardInterrupt:
        pass
