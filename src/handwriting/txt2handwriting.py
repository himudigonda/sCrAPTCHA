#! /usr/local/opt/python@3.9/bin/python3.9
# 2021-06-06 14:37:50
#! @author : @ruhend

import pywhatkit

debugFlag = 1


def __dout(status, output):
    if debugFlag:
        print(' ' + status + ' ' + output)
    else:
        pass


### Write Code From Here ###

pywhatkit.text_to_handwriting("Hello world! My name is Himansh Mudigonda","src/handwriting/alpha.py",[255,0,0])


### Code End Here ###
