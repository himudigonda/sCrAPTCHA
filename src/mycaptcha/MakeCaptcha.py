#! /usr/local/opt/python@3.9/bin/python3.9
# 2021-06-07 13:26:41
#! @author : @ruhend

# imports here
from captcha.image import *

# global variables here

__image_handler__ = ImageCaptcha()


### Write Code From Here ###
class MakeMyCaptcha:

    def _saveCaptchaAt(alphanumeric, LOC):
        __image_handler__ .write(alphanumeric, LOC)

    def _draftCaptcha(alphanumeric, LOC):
        __image_handler__ = ImageCaptcha()
        generated_captcha = __image_handler__ .generate(alphanumeric)
        MakeMyCaptcha._saveCaptchaAt(alphanumeric, LOC)

    if __name__ == '__main__':
        pass

### Code End Here ###
