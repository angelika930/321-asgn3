# Task 4
from minm_attack import *
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
    original = str(random.getrandbits(8)).encode('utf-8')

    start_time = time.perf_counter()
    start = 0
    count = 0
    org_brute_force = SHA256.new(original)
    org_brute_force = bin(int(org_brute_force.hexdigest(), 16))[2:10]
    brute_force = 0

    while brute_force != org_brute_force:
        count += 1
        start += 1
        brute_force = SHA256.new(str(start).encode('utf-8'))
        brute_force = bin(int(brute_force.hexdigest(), 16))[2:10]
    
    end_time = time.perf_counter()
    seconds = end_time - start_time

    print("Original:", int.from_bytes(original, byteorder='little'))
    print("Brute forced:", int(start))
    print("Collision found!")
    print("Hash Digest: ", brute_force)
    print("Count: ", count)
    print("Time: ", seconds)
    return





if __name__ == "__main__":
    print("--------------------------------------")
    find_collision(4)













