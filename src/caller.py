#!/usr/local/opt/python@3.9/bin/python3.9
# 2021-06-07 13:43:33
#! @author : @ruhend

import sys
import os
from captchaGenerator import captcha_generator as CG

debugFlag = 1


def __dout(status, output):
    if debugFlag:
        print(' ' + status + ' ' + output)
    else:
        pass


### Write Code From Here ###

# ! replace this with the randommly generated string
CG.captcha_generator.draftCaptcha('kjsjenf', "/Users/ruhend/Documents/GitHub/ruhend/projects/CAPTCHA/images/test.png")


### Code End Here ###
