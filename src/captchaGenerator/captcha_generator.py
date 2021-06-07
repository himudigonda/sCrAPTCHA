#! /usr/local/opt/python@3.9/bin/python3.9
# 2021-06-07 13:26:41
#! @author : @ruhend

from captcha.image import *

debugFlag = 1


def __dout(status, output):
    if debugFlag:
        print(' ' + status + ' ' + output)
    else:
        pass


### Write Code From Here ###
class captcha_generator:

    def saveCaptchaAt(code, LOC):
        image = ImageCaptcha()
        image.write(code, LOC)

    def draftCaptcha(code, LOC):

        image = ImageCaptcha()
        # image = ImageCaptcha(fonts=['../../fonts/a.ttf'])
        generated_captcha = image.generate(code)
        captcha_generator.saveCaptchaAt(code, LOC)

    if __name__ == '__main__':
        pass

### Code End Here ###
