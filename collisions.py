# Task 4
from minm_attack import *
from random import randint
from Crypto.Hash import SHA256
import time
import random

def collisions(input: bytes):
    input = input[:8]
    return input
    # print("Truncated input: ", input)
    # hash = SHA256.new(bytes(input.encode("utf8")))
    # print("Hashed input in hex:", hash.hexdigest())

def find_collision(num):  #takes in a number of bits to randomly generate
    di_dict = {}
    seconds = time.thread_time()
    count = 0
    while True:
        data = str(random.getrandbits(num)).encode('utf-8')
        hash = SHA256.new(data)
        digest = hash.hexdigest()
        digest = collisions(digest)
        if digest in di_dict:
            print("Collision found!")
            print("Hash Digest: ", digest)
            print("Count: ", count)
            print("Time: ", seconds)
            return
        
        di_dict[digest] = num
        count +=1




if __name__ == "__main__":
    print("--------------------------------------")
    find_collision(4)













