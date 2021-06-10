#! /usr/local/opt/python@3.9/bin/python3.9
# 2021-06-09 12:21:49
#! @author : @ruhend

# imports here


# global variables here
__AN_hash_dict__ = {'AlphaNumeric': 'SHA256'}

### Write Code From Here ###


class MakeMyDict():

    def Add2Dict(_received_code, _hash_of_code):
        i = 1
        __AN_hash_dict__[_received_code] = _hash_of_code
        # __AN_hash_dict__.append(_received_code, _hash_of_code)
        # __AN_hash_dict__

    def Print4romDict():
        print(__AN_hash_dict__)

    # Add2Dict('jsjdh', 'uiuewyr7u4ht78fsg6234')
    # Add2Dict('45uhsg', 'dscugyaui34hygdfads78')
    # Add2Dict('58uy', 'ei847598236y7iutghfgd')
    # Print4romDict()

    if __name__ == '__main__':
        pass

### Code End Here ###
