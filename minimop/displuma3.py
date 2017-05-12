from luma.core.interface.serial import i2c, spi
from luma.oled.device import ssd1306
import time

import sys
import random

#from demo_opts import get_device

import luma.core.render
from luma.core.sprite_system import framerate_regulator



def main(num_iterations=sys.maxsize):
    canvas = luma.core.render.canvas(device)
    width=128
    height=64
    while True:
        with canvas as c:
            for x in range(width-1):
                c.rectangle(device.bounding_box, outline="white", fill="black")
                c.line((x , 0) + (x, height-1), fill="white")
                time.sleep(1/25)
                

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
