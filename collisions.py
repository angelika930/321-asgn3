# Task 4
from minm_attack import *
from random import randint
from Crypto.Hash import SHA256
import time

def collisions(input: bytes):
    input = input[:8]
    return input
    #print("Truncated input: ", input)
    # hash = SHA256.new(bytes(input.encode("utf8")))
    # print("Hashed input in hex:", hash.hexdigest())

def find_collision():
    digest_dict = {}
    #byte_form = int(input)
    seconds = time.time()
    num = 13
    while True:
        d = num.to_bytes(length=(max(num.bit_length(),1) +7)//8, byteorder='big')
        hash = SHA256.new(d)
        digest = hash.hexdigest()
        digest = collisions(digest)
        if digest in digest_dict:
            print("Collision found!")
            print("Hash Digest: ", digest)
            print("Integer: ", num)
            print("Time: ", seconds)
            return
        else :
            num +=1
            digest_dict[digest] = num




if __name__ == "__main__":
    data_1 = "10"
    data_2 = "11"
    
    print("--------------------------------------")
    collisions(data_1)
    collisions(data_2)

    data_1 = '123456'
    data_2 = '023456'
    
    print("--------------------------------------")
    collisions(data_1)
    collisions(data_2)

    data_1 = '12345'
    data_2 = 'hellohello'
    
    print("--------------------------------------")
    collisions(data_1)
    collisions(data_2)

    print("--------------------------------------")
    find_collision()













