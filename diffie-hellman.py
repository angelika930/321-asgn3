# Task 1
# Answers Document: https://docs.google.com/document/d/19QCwZsk8nNX-VQG5AtfAyo1RBUetRGGEkAW0fyaeEbQ/edit?usp=sharing
# pip install pycryptodome

from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from random import randint
from Crypto.Hash import SHA256

BLOCK_SIZE = 16         # 128 bits


def calc_key(p,g, a) :      #p and g comes from sender
    val = g**(a)
    return val % p

def key_exchange(their_value,my_int,p) : #A is calculated by opposite party
    shared_key = bytes((their_value**my_int)%p)
    h = SHA256.new(data = shared_key)
    return h.hexdigest()

def create_cipher(message, key, iv):

    cipher = AES.new(key.encode("utf8"), AES.MODE_CBC, iv)
    cipher_text = cipher.encrypt(message)
    return cipher_text

def exchange_message(message, key, iv): #takes in the encrypted message
    cipher = AES.new(key.encode("utf8"), AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(message)
    decrypted = unpad(decrypted, BLOCK_SIZE)
    return decrypted

if __name__ == "__main__":
    p = 37
    g = 5
    iv = get_random_bytes(16)
    alice_a = randint(1, p-2)
    alice = calc_key(p, g, alice_a)
    bob_b = randint(1, p-2)
    bob = calc_key(p, g, bob_b)

    alice_key = bin(int(key_exchange(bob, alice_a, p), 16))[2:18]
    bob_key = bin(int(key_exchange(alice, bob_b, p),16))[2:18]
 
    print("Alice's key:", alice_key)
    print("Bob's key:", bob_key)
    print("Same?", alice_key == bob_key)
    print("Alice's cipher:", create_cipher(pad(b"hi bob", 16), str(alice_key), iv))
    print("Bob's cipher:", create_cipher(pad(b"hi alice", 16), str(bob_key), iv))

    a_msg = create_cipher(pad(b"hi bob", 16), str(alice_key), iv)
    b_msg = create_cipher(pad(b"hi alice", 16), str(bob_key), iv)
    print("Bob's decrypted message: ", exchange_message(b_msg, str(bob_key), iv))
    print("Alice's decrypted message: ", exchange_message(a_msg, str(alice_key), iv))
