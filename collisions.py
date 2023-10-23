# Task 4
from minm_attack import *
from Crypto.Random import get_random_bytes
from random import randint
from Crypto.Hash import SHA256

data = get_random_bytes(16)
print("data:", data)
h = SHA256.new(data)
print("hex:", h.hexdigest())

string1 = "Hello man"
string1 = string1.encode('utf-8')
h = SHA256.new(bytes(string1))
print("Original digest: " ,  h.hexdigest())
string2 = "Hell man"
string2 = string2.encode('utf-8')
h = SHA256.new(bytes(string2))
print("New digest: " , h.hexdigest())






