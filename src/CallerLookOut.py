#!/usr/local/opt/python@3.9/bin/python3.9
# 2021-06-07 13:43:33
#! @author : @ruhend

# imports here
from json import dump
from mycaptcha import MakeCaptcha
from mycode import MakeCode
from myhasher import MakeHash
from mydict import MakeMyDict
from mydumpinJSON import DumpInJSON

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
        dict_maker_handler = MakeMyDict.MakeMyDict
        json_dict_handler = DumpInJSON.DumpInJSON

        # Make alphanumeric code
        _received_code = code_maker_handler._generate_alphanumeric()

        # Calculate Hash of alphanumeric code
        hash_of_code = hash_maker_handler._HashTheCode(_received_code)
        print(_received_code + ':' + hash_of_code)

        # Make a dictionary of the values
        temp_dict = dict_maker_handler.MakeDictCom(hash_of_code, _received_code)
        print('>',temp_dict)
        
        # Dump the dictionary in json
        json_dict_handler.JSONAppender(temp_dict)
        # json_dict_handler.JSONDumper(temp_dict)

        #! Change this later on to recurring file name numbers.
        _save_captcha_location = __automated_path__+__file_name__

        # Save Captcha @_save_captcha_location
        captcha_maker_handler._draftCaptcha(
            _received_code, _save_captcha_location)

    if __name__ == '__main__':
        # dict_maker_handler = MakeMyDict.MakeMyDict

        # Input your number of files here
        _net_captchas = 100
        for _each_captcha in range(0, _net_captchas):
            MainContainer(_each_captcha)
        # dict_maker_handler.Print4romDict()


### Code End Here ###
