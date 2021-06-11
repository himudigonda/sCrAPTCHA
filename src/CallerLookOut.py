#!/usr/local/opt/python@3.9/bin/python3.9
# 2021-06-07 13:43:33
#! @author : @ruhend

# imports here
from ast import Call
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
code_maker_handler = MakeCode.MakeMyCode
captcha_maker_handler = MakeCaptcha.MakeMyCaptcha
hash_maker_handler = MakeHash.MakeHash
dict_maker_handler = MakeMyDict.MakeMyDict
json_dict_handler = DumpInJSON.DumpInJSON


class CallerLookOut:

    def RecieveCode(self):
        self.recieved_code = code_maker_handler._generate_alphanumeric()
        return self.recieved_code

    def HashOfCode(self, _received_code):
        self.hash_of_code = hash_maker_handler._HashTheCode(_received_code)
        return self.hash_of_code

    # def Template(self,_received_code):
    #     self.name = constructor.function(argument)
    #     return self.name

    def DictMaker(self, hash_of_code, _received_code):
        self.dict = dict_maker_handler.MakeDictCom(
            hash_of_code, _received_code)
        return self.dict

    def JSONBuilder(self, temp_dict):
        json_dict_handler.JSONAppender(temp_dict)

    def MakeNSaveCaptcha(self, _received_code, _save_captcha_location):
        captcha_maker_handler._draftCaptcha(
            _received_code, _save_captcha_location)

    def MainContainer(self, _file_number):
        __file_name__ = __file_domain__+str(_file_number)+__file_extension__
        _save_captcha_location = __automated_path__+__file_name__

        # Make alphanumeric code
        _received_code = CallerLookOut.RecieveCode(self)

        # Calculate Hash of alphanumeric code
        hash_of_code = CallerHandler.HashOfCode(_received_code)
        # print(_received_code + ':' + hash_of_code)

        # Make a dictionary of the values
        temp_dict = CallerHandler.DictMaker(hash_of_code, _received_code)
        # print('>', temp_dict)

        # Dump the dictionary in json
        CallerHandler.JSONBuilder(temp_dict)
        # json_dict_handler.JSONDumper(temp_dict)

        # Save Captcha @_save_captcha_location
        CallerHandler.MakeNSaveCaptcha(_received_code, _save_captcha_location)


CallerHandler = CallerLookOut()
_net_captchas = 2
for _each_captcha in range(0, _net_captchas):
    CallerHandler.MainContainer(_each_captcha)
    # dict_maker_handler.Print4romDict()


### Code End Here ###
