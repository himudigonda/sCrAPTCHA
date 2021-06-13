
# 2021-06-08 11:56:09
#! @author : @ruhend

# imports here
import hashlib

# global variables here

### Write Code From Here ###


class MakeHash:
    def _EncodeString(_string):
        encoded_string = _string.encode()
        return encoded_string

    def _SHA256This(_string):
        sha256ed = hashlib.sha256(_string)
        return sha256ed

    def _HashTheAlphanumeric(_string):
        hashed_value = MakeHash._SHA256This(MakeHash._EncodeString(_string))
        hashed_value_in_hex = hashed_value.hexdigest()
        return hashed_value_in_hex

    if __name__ == '__main__':
        pass


### Code Ends Here ###
