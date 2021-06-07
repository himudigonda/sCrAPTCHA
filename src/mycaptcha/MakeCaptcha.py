#! /usr/local/opt/python@3.9/bin/python3.9
# 2021-06-07 13:26:41
#! @author : @ruhend

from captcha.image import *

__debugFlag__ = 1


def __dout(status, output):
    if __debugFlag__:
        print(' ' + status + ' ' + output)
    else:
        pass

__image_handler__ = ImageCaptcha()


### Write Code From Here ###
class MakeMyCaptcha:

    def _saveCaptchaAt(code, LOC):
        __image_handler__ .write(code, LOC)

    def _draftCaptcha(code, LOC):
        __image_handler__  = ImageCaptcha()
        generated_captcha = __image_handler__ .generate(code)
        MakeMyCaptcha._saveCaptchaAt(code, LOC)

    if __name__ == '__main__':
        pass

### Code End Here ###
