#!/usr/local/opt/python@3.9/bin/python3.9
# 2021-06-07 13:43:33
#! @author : @ruhend

# imports here
from mycaptcha import MakeCaptcha
from mycode import MakeCode
from myhasher import MakeHash

# global variables here

### Write Code From Here ###
# __file_number__ = 0
__automated_path__ = '/Users/ruhend/Documents/GitHub/ruhend/projects/sCrAPTCHA/images/tests/'
__file_domain__ = 'automated_image'
__file_extension__ = '.png'


class CallerLookOut:

    def MainContainer(_file_number):
        __file_name__ = __file_domain__+str(_file_number)+__file_extension__
    # Constructors
        code_maker_handler = MakeCode.MakeMyCode
        captcha_maker_handler = MakeCaptcha.MakeMyCaptcha
        hash_maker_handler = MakeHash.MakeHash

        # Make alphanumeric code
        _received_code = code_maker_handler._generate_alphanumeric()

        # Calculate Hash of alphanumeric code
        hash_of_code = hash_maker_handler._HashTheCode(_received_code)
        print(_received_code + ':' + hash_of_code)

        #! Change this later on to recurring file name numbers.
        _save_captcha_location = __automated_path__+__file_name__

        # Save Captcha @_save_captcha_location
        captcha_maker_handler._draftCaptcha(
            _received_code, _save_captcha_location)

    if __name__ == '__main__':
        # Input your number of files here
        _net_captchas = 5
        for _each_captcha in range(0, _net_captchas):
            MainContainer(_each_captcha)


### Code End Here ###
