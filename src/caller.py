#!/usr/local/opt/python@3.9/bin/python3.9
# 2021-06-07 13:43:33
#! @author : @ruhend

from captchaGenerator import captcha_generator as CG
from stringGenerator import init_str_gen as isg

debugFlag = 1


def __dout(status, output):
    if debugFlag:
        print(' ' + status + ' ' + output)
    else:
        pass


### Write Code From Here ###

# ! replace this with the randommly generated string
random_String = isg.init_cap_gen.genstr()
# print(random_String)
CG.captcha_generator.draftCaptcha(
    random_String, "/Users/ruhend/Documents/GitHub/ruhend/projects/CAPTCHA/images/tests/automated_image.png")
# CG.captcha_generator.draftCaptcha('kjsjenf', "/Users/ruhend/Documents/GitHub/ruhend/projects/CAPTCHA/images/test.png")


### Code End Here ###
