# Task 1
# Answers Document: https://docs.google.com/document/d/19QCwZsk8nNX-VQG5AtfAyo1RBUetRGGEkAW0fyaeEbQ/edit?usp=sharing
# pip install pycryptodome

from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from random import randint
from Crypto.Hash import SHA256

BLOCK_SIZE = 16         # 128 bits

def calc_key(p,g) :      #p and g comes from sender
    secret_value = randint(1, p-2)
    val = g**(secret_value)
    return val % p

def key_exchange(A,a,p) : #A is calculated by opposite party
    key = (A**a)%p
    h = SHA256.new()
    h.update(key)