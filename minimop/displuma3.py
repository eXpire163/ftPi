from luma.core.interface.serial import i2c, spi
from luma.oled.device import ssd1306

import time
import sys
import random

#from demo_opts import get_device

import luma.core.render
from luma.core.sprite_system import framerate_regulator



def main():
    canvas = luma.core.render.canvas(device)
    width=127
    height=63
    
    regulator = framerate_regulator(fps=0)
    
    frame_count = 0
    fps = ""
    
    
    while True:
        with regulator:
            for x in range(width-1):
                with canvas as c:
                    frame_count += 1
                    c.rectangle(device.bounding_box, outline="white", fill="black")
                    print(device.bounding_box)
                    c.line((x , 0) + (x, height-1), fill="red")
                    #c.ellipse((x+5, 15, x+15, 25), fill="red")
                    print("drawline {}".format(x))
                    c.text((2, 0), fps, fill="white")
                    #time.sleep(1)
                
                if frame_count % 20 == 0:
                    fps = "FPS: {0:0.3f}".format(regulator.effective_FPS())

if __name__ == '__main__':
    try:

        # rev.1 users set port=0
        # substitute spi(device=0, port=0) below if using that interface
        serial = i2c(port=1, address=0x3C)
        # substitute ssd1331(...) or sh1106(...) below if using that device
        device = ssd1306(serial)

        
        main()
    except KeyboardInterrupt:
        pass
