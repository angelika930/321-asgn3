# Task 1
# Answers Document: https://docs.google.com/document/d/19QCwZsk8nNX-VQG5AtfAyo1RBUetRGGEkAW0fyaeEbQ/edit?usp=sharing
# pip install pycryptodome

from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

BLOCK_SIZE = 16         # 128 bits
