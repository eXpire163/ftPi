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
    from luma.emulator.device import emulator
    testenv = True




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
        else:
            device = emulator(width=128, height=64, rotate=0, mode='1', transform='none', scale=6)
        
        
        main()
    except KeyboardInterrupt:
        pass
