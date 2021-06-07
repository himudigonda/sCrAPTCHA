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


### Write Code From Here ###
class MakeMyCaptcha:

    def _saveCaptchaAt(code, LOC):
        image = ImageCaptcha()
        image.write(code, LOC)

    def _draftCaptcha(code, LOC):

        image = ImageCaptcha()
        generated_captcha = image.generate(code)
        MakeMyCaptcha._saveCaptchaAt(code, LOC)

    if __name__ == '__main__':
        pass

### Code End Here ###
