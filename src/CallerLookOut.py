
# 2021-06-07 13:43:33
#! @author : @ruhend

# imports here
from mycaptcha import MakeCaptcha
from myalphanumeric import MakeAlphanumeric
from myhasher import MakeHash
from mydict import MakeMyDict
from mydumpinJSON import DumpInJSON
from myimageputter import PutMyImage
from myuserinput import UserInput

# global variables here
__project_location__ = '/home/ruhend/Documents/GitHub/ruhend/projects/sCrAPTCHA'
__automated_path__ = __project_location__+'/images/tests'
__file_domain__ = 'automated_image'
__file_extension__ = '.png'
alphanumeric_maker_handler = MakeAlphanumeric.MakeMyAlphanumeric
captcha_maker_handler = MakeCaptcha.MakeMyCaptcha
hash_maker_handler = MakeHash.MakeHash
dict_maker_handler = MakeMyDict.MakeMyDict
json_dict_handler = DumpInJSON.DumpInJSON
image_putter_handler = PutMyImage.PutMyImage
user_input_handler = UserInput.UserInput

# template function
# def Template(self,_received_alphanumeric):
#     self.name = constructor.function(argument)
#     return self.name


### Write Code From Here ###

class CallerLookOut:

    def RecieveAlphanumeric(self):
        self.recieved_alphanumeric = alphanumeric_maker_handler._generate_alphanumeric()
        return self.recieved_alphanumeric

    def HashOfAlphanumeric(self, _received_alphanumeric):
        self.hash_of_alphanumeric = hash_maker_handler._HashTheAlphanumeric(
            _received_alphanumeric)
        return self.hash_of_alphanumeric

    def DictMaker(self, hash_of_alphanumeric, _received_alphanumeric):
        self.dict = dict_maker_handler.MakeDictCom(
            hash_of_alphanumeric, _received_alphanumeric)
        return self.dict

    def JSONBuilder(self, temp_dict):
        json_dict_handler.JSONAppender(temp_dict)

    def MakeNSaveCaptcha(self, _received_alphanumeric, _save_captcha_location):
        captcha_maker_handler._draftCaptcha(
            _received_alphanumeric, _save_captcha_location)

    def ImagePutter(self, _path_to_alphanumeric_image):
        image_putter_handler.ThrowImage(_path_to_alphanumeric_image)

    def GetUserInput(self):
        self.user_input_alphanumeric = user_input_handler.GetUserInput()
        return self.user_input_alphanumeric


    def MainContainer(self):
        __file_name__ = __file_domain__+__file_extension__
        _save_captcha_location = __automated_path__+__file_name__

        # Make alphanumeric alphanumeric
        _received_alphanumeric = CallerLookOut.RecieveAlphanumeric(self)
        print("Generated Captcha         : "+str(_received_alphanumeric))

        # Calculate Hash of alphanumeric alphanumeric
        hash_of_alphanumeric = CallerHandler.HashOfAlphanumeric(
            _received_alphanumeric)
        print("Generated Captcha Hash    : "+str(hash_of_alphanumeric))
        # print(_received_alphanumeric + ':' + hash_of_alphanumeric)

        # Make a dictionary of the values
        temp_dict = CallerHandler.DictMaker(
            hash_of_alphanumeric, _received_alphanumeric)
        # print('>', temp_dict)

        # Dump the dictionary in json
        CallerHandler.JSONBuilder(temp_dict)
        # json_dict_handler.JSONDumper(temp_dict)

        # Save Captcha @_save_captcha_location
        CallerHandler.MakeNSaveCaptcha(
            _received_alphanumeric, _save_captcha_location)

        # Shows randomly generated alphanumeric string in default image viewer client
        # image_out_process = Process(traget = CallerHandler.ImagePutter(_save_captcha_location))
        CallerHandler.ImagePutter(_save_captcha_location)
         
        # Gets user input alphanumeric
        user_input = CallerHandler.GetUserInput()

        # Calculate has of user input
        hash_of_user_input = CallerHandler.HashOfAlphanumeric(user_input)
        print("User Input Hash           : "+str(hash_of_user_input))
        
CallerHandler = CallerLookOut()
CallerHandler.MainContainer()


### Code Ends Here ###
