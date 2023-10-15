from random import randint
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
def calc_key(p,g) :      #p and g comes from sender
    secret_value = randint(1, p-2)
    val = g**(secret_value)
    return val % p

def key_exchange(A,a,p) : #A is calculated by opposite party
    key = (A**a)%p
    h = SHA256.new()
    h.update(key)
