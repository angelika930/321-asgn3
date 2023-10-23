# Task 4
from minm_attack import *
from random import randint
from Crypto.Hash import SHA256

def collisions(input: bytes):
    input = input[:8]
    print("Truncated input: ", input)
    hash = SHA256.new(bytes(input.encode("utf8")))
    print("Hashed input in hex:", hash.hexdigest())

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

    data_1 = 'Hellohello'
    data_2 = 'hellohello'
    
    print("--------------------------------------")
    collisions(data_1)
    collisions(data_2)





string1 = "Hello man"
string1 = string1.encode('utf-8')
h = SHA256.new(bytes(string1))
print("Original digest: " ,  h.hexdigest())
string2 = "Hell man"
string2 = string2.encode('utf-8')
h = SHA256.new(bytes(string2))
print("New digest: " , h.hexdigest())






