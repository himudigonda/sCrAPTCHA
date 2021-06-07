#! /usr/local/opt/python@3.9/bin/python3.9
# 2021-06-07 16:53:34
#! @author : @ruhend

import random
import string
import re


debugFlag = 1


def __dout(status, output):
    if debugFlag:
        print(' ' + status + ' ' + output)
    else:
        pass


### Write Code From Here ###
class init_cap_gen:

    def genlength():
        maxLength = [4, 5, 6, 7]
        pickNumber = random.choice(maxLength)
        return pickNumber
    # init_cap_gen.genstr(pickNumber)

    def genstr():
        lengthOfCaption = init_cap_gen.genlength()
        defRange = 'abcdefghjiklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*\(\)'
        randomStr = ''.join(random.choice(defRange)
                            for letters in range(lengthOfCaption))
        return randomStr

    # genlength()
    # length_of_captcha = genlength()
    # print(init_cap_gen.genstr(length_of_captcha))
    if __name__ == '__main__':
        pass

# print(genlength())
### Code End Here ###
