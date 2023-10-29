# Task 4 option 2
from random import *
from Crypto.Hash import SHA256
import time

def collisions(input: bytes):
    input = input[:8]
    return input
    # print("Truncated input: ", input)
    # hash = SHA256.new(bytes(input.encode("utf8")))
    # print("Hashed input in hex:", hash.hexdigest())

def find_collision(num):  #takes in a number of bits to randomly generate
    original = str(random.getrandbits(randint(0, 256))).encode('utf-8')
    print(original)
    hash = SHA256.new(original)

    start_time = time.perf_counter()
    start = 0
    count = 0
    brute_force = SHA256.new(str(start).encode('utf-8'))
    while brute_force.hexdigest()[:8] != hash.hexdigest()[:8]:
        count +=1
        start += 1
        brute_force = SHA256.new(str(start).encode('utf-8'))
    
    end_time = time.perf_counter()
    seconds = end_time - start_time

    print("Original:", int.from_bytes(original, byteorder='little'))
    print("Brute forced:", int(start))
    print("Collision found!")
    print("Hash Digest: ", brute_force.hexdigest())
    print("Count: ", count)
    print("Time: ", seconds)
    return

def find_collision_dict(num):
    digest_dict = {}
    start = 0
    count = 0
    start_time = time.perf_counter()
    brute_force = SHA256.new(str(start).encode('utf-8'))
    
    brute_force = bin(int(brute_force.hexdigest(), 16))[2:num+2]

    while digest_dict.get(brute_force) == None:
        digest_dict[brute_force] = start
        count += 1
        start += 1
        brute_force = SHA256.new(str(start).encode('utf-8'))
        brute_force = bin(int(brute_force.hexdigest(), 16))[2:num+2]
    
    end_time = time.perf_counter()
    seconds = end_time - start_time
    #print("Collision found!")
    print("Original message:", digest_dict[brute_force])
    print("Hash Digest: ", brute_force)
    print("Number of inputs: ", count)              # also Brute Forced Message
    print("Time: ", seconds)
    return digest_dict

if __name__ == "__main__":
    for x in range(8, 51, 2):
        print("--------------------------------------")
        print("Digest size:", x)
        find_collision_dict(x)
    #print(find_collision_dict(8))













