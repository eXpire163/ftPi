from lib.Eyes import Eyes

#from demo_opts import get_device


try:
    import luma.core.render
    from luma.core.sprite_system import framerate_regulator
    from luma.core.interface.serial import i2c
    from luma.oled.device import ssd1306
    TESTENV = False
except ImportError:
    #from luma.emulator.device import emulator
    TESTENV = True




def main():
    #colors = ["red", "orange", "yellow", "green", "blue", "magenta"]
    eyes = Eyes()

    eyes.set_action("blinzeln", 3.0)

    frame_count = 0
    fps = ""

    if(not TESTENV):
        canvas = luma.core.render.canvas(DEVICE)
        regulator = framerate_regulator(fps=5)

    while not TESTENV:
        with regulator:

            frame_count += 1
            with canvas as can:
                can.rectangle(DEVICE.bounding_box, fill="black")
                eyes.update_pos()
                eyes.draw(can)
                can.text((2, 0), fps, fill="white")

            if frame_count % 20 == 0:
                fps = "FPS: {0:0.3f}".format(regulator.effective_FPS())
    while TESTENV:
        eyes.update_pos()
        print(eyes.get_status())


if __name__ == '__main__':
    try:
        if(not TESTENV):
            # rev.1 users set port=0
            # substitute spi(device=0, port=0) below if using that interface
            SERIAL = i2c(port=1, address=0x3C)
            # substitute ssd1331(...) or sh1106(...) below if using that device
            DEVICE = ssd1306(SERIAL)
        else:
            pass
            #device = emulator(width=128, height=64, rotate=0, mode='1', transform='none', scale=6)


        main()
    except KeyboardInterrupt:
        pass
