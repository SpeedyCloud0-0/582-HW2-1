import hashlib
import os
import random
import string

length = 10


def hash_collision(k):
    if not isinstance(k, int):
        print("hash_collision expects an integer")
        return b'\x00', b'\x00'
    if k < 0:
        print("Specify a positive number of bits")
        return b'\x00', b'\x00'

    # Collision finding code goes here
    x = b'\x00'
    y = b'\x00'

    # Create a random string
    test_str = get_random_string(length)

    # Sha256 the string and then get the last k digits of the result
    sha_str = get_sha_last_digit(test_str, k)

    # Create a dictionary that stores the original string and the hex returned by sha256
    check_dict = dict(sha_str=test_str)

    while True:
        test_str = get_random_string(length)
        sha_str = get_sha_last_digit(test_str, k)
        if sha_str not in check_dict:
            check_dict[sha_str] = test_str
        else:
            x = test_str
            y = check_dict.get(sha_str)
            break
            
    return x, y


def get_random_string(len):
    letters = string.ascii_letters
    result_str = str.encode(''.join(random.choice(letters) for i in range(len)))
    return result_str


def get_sha_last_digit(word, num):
    sha_str = hashlib.sha256(word).hexdigest()
    last_digits = sha_str[-num:]
    return last_digits

#
# hash_collision(3)
