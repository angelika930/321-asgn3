# Task 4
from minm_attack import *
from Crypto.Random import get_random_bytes
from random import randint
from Crypto.Hash import SHA256

data = get_random_bytes(16)
print("data:", data)
h = SHA256.new(data)
print("hex:", h.hexdigest())



