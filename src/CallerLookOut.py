#!/usr/local/opt/python@3.9/bin/python3.9
# 2021-06-07 13:43:33
#! @author : @ruhend

from mycaptcha import MakeCaptcha
from mycode import MakeCode

__debugFlag__ = 1


def __dout(status, output):
    if __debugFlag__:
        print(' ' + status + ' ' + output)
    else:
        pass


### Write Code From Here ###

__automated_path__ = '/Users/ruhend/Documents/GitHub/ruhend/projects/CAPTCHA/images/tests/'
__file_name__ = 'automated_image.png'


class CallerLookOut:

    def MainContainer():
        code_maker_handler = MakeCode.MakeMyCode
        captcha_maker_handler = MakeCaptcha.MakeMyCaptcha
        received_code = code_maker_handler._generate_alphanumeric()
        save_captcha_location = __automated_path__+__file_name__
        captcha_maker_handler._draftCaptcha(
            received_code, save_captcha_location)

    if __name__ == '__main__':
        MainContainer()


### Code End Here ###
