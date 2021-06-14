
# 2021-06-11 15:40:43
#! @author : @ruhend

# imports here
import time
from PIL import Image
import psutil

# global variables here

### Write Code From Here ###


class PutThisImage:

    def CloseImageWindow():
        time.sleep(0.5)
        for proc in psutil.process_iter():
            if proc.name() == 'display':
                proc.terminate()
                proc.kill()

    def ThrowImage(_path):
        try:
            image_to_print = Image.open(_path)
            image_to_print.show()
            # PutMyImage.CloseImageWindow()
            # print(image_to_print.histogram)
        except IOError:
            print(" - Couldn't find image at $_path")

    if __name__ == '__main__':
        pass


### Code End Heres ###
