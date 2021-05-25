import hashlib
import os

length = 20


def hash_preimage(target_string):
    if not all( [x in '01' for x in target_string ] ):
        print( "Input should be a string of bits" )
        return
    nonce = b'\x00'

    tra_length = len(target_string)

    # Create a random byte
    test_str = os.urandom(length)

    # Sha256 the string and then get the last k digits of the result
    sha_str = get_sha_last_digit(test_str, tra_length)

    while sha_str != target_string:
        test_str = os.urandom(length)
        sha_str = get_sha_last_digit(test_str, tra_length)

    nonce = test_str
    # print(nonce)
    return nonce


def get_sha_last_digit(word, num):
    sha_str = hashlib.sha256(word).hexdigest()
    last_digits = sha_str[-num:]
    return last_digits


# hash_preimage('001100')
