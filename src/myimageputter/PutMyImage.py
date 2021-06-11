#! /usr/local/opt/python@3.9/bin/python3.9
# 2021-06-11 15:40:43
#! @author : @ruhend

# imports here
from PIL import Image

# global variables here

### Write Code From Here ###


class PutMyImage:

    def ThrowImage(_path):
        try:
            image_to_print = Image.open(_path)
            image_to_print.show()
            # print(image_to_print.histogram)
        except IOError:
            print(" - Couldn't find image at $_path") 

    if __name__ == '__main__':
        pass

    ThrowImage(r'../../images/tests/automated_image0.png')

### Code End Here ###
