
# 2021-06-09 12:01:55
#! @author : @ruhend

# imports here
import json
import pickle

# global variables here
__AN_hash_dict__ = {'AlphaNumeric': 'SHA256'}

### Write Code From Here ###


class DumpInJSON():

    __save_json_at_ = '../../Storage/AN-HASH_json.json'

   # def PickleDumper(_alphanumeric_hash_dict):
   #     with open('AN-HASH_pickle.json', 'wb') as fp:
   #         pickle.dump(_alphanumeric_hash_dict, fp)

    def JSONDumper(_alphanumeric_hash_dict):
        with open("../Storage/AN-HASH_json.json", 'w') as rp:
            json.dump(_alphanumeric_hash_dict, rp)

    def JSONAppender(_alphanumeric_hash_dict):
        with open("../Storage/AN-HASH_json.json", 'r+') as JSONFile:
            data = json.load(JSONFile)
            data.update(_alphanumeric_hash_dict)
            JSONFile.seek(0)
            json.dump(data, JSONFile)

    # temp_dict = {'sdfasdf':'sduyq234h5iufhsgu2y3u4ihj5hrgyfgasdfguq234',
    #              'dfjgh':'wu4y97berwutyqnv9384t3ydsktupq24oiu2gsdg'
    #              }
    # JSONDumper(temp_dict)

    if __name__ == '__main__':
        # JSONDumper(__AN_hash_dict__)
        pass

### Code Ends Here ###
