#! /usr/local/opt/python@3.9/bin/python3.9
# 2021-06-07 16:53:34
#! @author : @ruhend

# imports here
import random
import string
import re


# global variables here
__numeric_options__ = [4, 5, 6, 7]
__alphanumeric_options__ = 'abcdefghijkmnoqrstuvwxyzABCDEFGHKLMNOPQRSTUVWXYZ0123456789'

### Write Code From Here ###


class MakeMyCode:

    def _generate_length():
        random_number = random.choice(__numeric_options__)
        return random_number

    def _generate_alphanumeric():
        caption_length = MakeMyCode._generate_length()
        random_alphanumeric = ''.join(random.choice(__alphanumeric_options__)
                                      for letters in range(caption_length))
        return random_alphanumeric

    if __name__ == '__main__':
        pass

#
### Code End Here ###
