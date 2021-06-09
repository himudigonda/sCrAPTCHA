#! /usr/local/opt/python@3.9/bin/python3.9
# 2021-06-09 12:01:55
#! @author : @ruhend

# imports here
import json
import pickle

# global variables here
__save_json_at_ = '../../storage/AN-HASH_json.json'

### Write Code From Here ###


class DumpInJSON():

    # def PickleDumper(_alphanumeric_hash_dict):
    #     with open('AN-HASH_pickle.json', 'wb') as fp:
    #         pickle.dump(_alphanumeric_hash_dict, fp)

    def JSONDumper(_alphanumeric_hash_dict):
        with open('AN-HASH_json.json', 'w') as rp:
            json.dump(_alphanumeric_hash_dict, rp)

    # temp_dict = {'sdfasdf':'sduyq234h5iufhsgu2y3u4ihj5hrgyfgasdfguq234',
    #              'dfjgh':'wu4y97berwutyqnv9384t3ydsktupq24oiu2gsdg'
    #              }
    # JSONDumper(temp_dict)

    if __name__ == '__main__':
        pass

### Code End Here ###
