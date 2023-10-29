    # find_collision(4)
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from random import randint
from Crypto.Hash import SHA256
from diffie_hellman import *

hash = SHA256.new(bytes(int('10111111',2)))
print(hash.hexdigest())

hash = SHA256.new(bytes(int('10110001',2)))
print(hash.hexdigest())