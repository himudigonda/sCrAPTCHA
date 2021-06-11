#!/usr/local/opt/python@3.9/bin/python3.9
# 2021-06-07 13:43:33
#! @author : @ruhend

# imports here
from ast import Call
from json import dump
from mycaptcha import MakeCaptcha
from myalphanumeric import MakeAlphanumeric
from myhasher import MakeHash
from mydict import MakeMyDict
from mydumpinJSON import DumpInJSON

# global variables here

### Write Code From Here ###
# __file_number__ = 0
__automated_path__ = '/Users/ruhend/Documents/GitHub/ruhend/projects/sCrAPTCHA/images/tests/'
__file_domain__ = 'automated_image'
__file_extension__ = '.png'
alphanumeric_maker_handler = MakeAlphanumeric.MakeMyAlphanumeric
captcha_maker_handler = MakeCaptcha.MakeMyCaptcha
hash_maker_handler = MakeHash.MakeHash
dict_maker_handler = MakeMyDict.MakeMyDict
json_dict_handler = DumpInJSON.DumpInJSON


class CallerLookOut:

    def RecieveAlphanumeric(self):
        self.recieved_alphanumeric = alphanumeric_maker_handler._generate_alphanumeric()
        return self.recieved_alphanumeric

    def HashOfAlphanumeric(self, _received_alphanumeric):
        self.hash_of_alphanumeric = hash_maker_handler._HashTheAlphanumeric(_received_alphanumeric)
        return self.hash_of_alphanumeric

    # def Template(self,_received_alphanumeric):
    #     self.name = constructor.function(argument)
    #     return self.name

    def DictMaker(self, hash_of_alphanumeric, _received_alphanumeric):
        self.dict = dict_maker_handler.MakeDictCom(
            hash_of_alphanumeric, _received_alphanumeric)
        return self.dict

    def JSONBuilder(self, temp_dict):
        json_dict_handler.JSONAppender(temp_dict)

    def MakeNSaveCaptcha(self, _received_alphanumeric, _save_captcha_location):
        captcha_maker_handler._draftCaptcha(
            _received_alphanumeric, _save_captcha_location)

    def MainContainer(self, _file_number):
        __file_name__ = __file_domain__+str(_file_number)+__file_extension__
        _save_captcha_location = __automated_path__+__file_name__

        # Make alphanumeric alphanumeric
        _received_alphanumeric = CallerLookOut.RecieveAlphanumeric(self)

        # Calculate Hash of alphanumeric alphanumeric
        hash_of_alphanumeric = CallerHandler.HashOfAlphanumeric(_received_alphanumeric)
        # print(_received_alphanumeric + ':' + hash_of_alphanumeric)

        # Make a dictionary of the values
        temp_dict = CallerHandler.DictMaker(hash_of_alphanumeric, _received_alphanumeric)
        # print('>', temp_dict)

        # Dump the dictionary in json
        CallerHandler.JSONBuilder(temp_dict)
        # json_dict_handler.JSONDumper(temp_dict)

        # Save Captcha @_save_captcha_location
        CallerHandler.MakeNSaveCaptcha(_received_alphanumeric, _save_captcha_location)


CallerHandler = CallerLookOut()
_net_captchas = 2
for _each_captcha in range(0, _net_captchas):
    CallerHandler.MainContainer(_each_captcha)
    # dict_maker_handler.Print4romDict()


### Code End Here ###
