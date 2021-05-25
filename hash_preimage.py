import hashlib
import os
import random
import string

length = 10


def hash_preimage(target_string):
    if not all( [x in '01' for x in target_string ] ):
        print( "Input should be a string of bits" )
        return
    nonce = b'\x00'

    tra_length = len(target_string)

    # Create a random string
    test_str = get_random_string(length)

    # Sha256 the string and then get the last k digits of the result
    sha_str = get_sha_last_digit(test_str, tra_length)

    while sha_str != target_string:
        test_str = get_random_string(length)
        sha_str = get_sha_last_digit(test_str, tra_length)

    nonce = test_str
    return nonce


def get_random_string(len):
    letters = string.ascii_letters
    result_str = str.encode(''.join(random.choice(letters) for i in range(len)))
    return result_str


def get_sha_last_digit(word, num):
    sha_str = hashlib.sha256(word).hexdigest()
    last_digits = sha_str[-num:]
    return last_digits

# hash_preimage('01000')
