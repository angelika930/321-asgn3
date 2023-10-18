# Task 2
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from random import randint
from Crypto.Hash import SHA256
from diffie_hellman import *

def minm_attack_on_keys():
    iv = get_random_bytes(16)   

    # tampering with keys (Task 2A)
    mallory_key = 1010111101010101              # random 16 byte key
    alice_key = mallory_key
    bob_key = mallory_key

    alice_cipher = create_cipher(pad(b"hi bob", 16), str(alice_key), iv)
    bob_cipher = create_cipher(pad(b"hi alice", 16), str(bob_key), iv)

    print("Alice's cipher:", alice_cipher)
    print("Bob's cipher:", bob_cipher)
    print("Alice's decrypted message: ", exchange_message(alice_cipher, str(alice_key), iv))
    print("Bob's decrypted message: ", exchange_message(bob_cipher, str(bob_key), iv))
    print("Mallory's decrypted message (from Alice): ", exchange_message(alice_cipher, str(mallory_key), iv))
    print("Mallory's decrypted message (from Bob): ", exchange_message(bob_cipher, str(mallory_key), iv))

    
def minm_attack_on_g(p, g):
    iv = get_random_bytes(16)
    alice_a = randint(1, p-2)
    alice = calc_key(p, g, alice_a)
    bob_b = randint(1, p-2)
    bob = calc_key(p, g, bob_b)

    alice_key = bin(int(key_exchange(bob, alice_a, p), 16))[2:18]
    bob_key = bin(int(key_exchange(alice, bob_b, p),16))[2:18]

    alice_cipher = create_cipher(pad(b"hi bob", 16), str(alice_key), iv)
    bob_cipher = create_cipher(pad(b"hi alice", 16), str(bob_key), iv)

    print("Alice's cipher:", alice_cipher)
    print("Bob's cipher:", bob_cipher)
    print("Bob's decrypted message: ", exchange_message(bob_cipher, str(bob_key), iv))
    print("Alice's decrypted message: ", exchange_message(alice_cipher, str(alice_key), iv))

    #tampering with g (Task 2B)
    if p == g:
        h = SHA256.new(data = bytes(0))
    elif g == 1:
        h = SHA256.new(data = bytes(1))
    elif g == p-1:
        if (alice_a % 2 == 0):
            h = SHA256.new(data = bytes(1))
        else:
            h = SHA256.new(data = bytes(p-1))
    mallory_key = bin(int(h.hexdigest(),16))[2:18]
    print("Mallory's decrypted message (from Alice): ", exchange_message(alice_cipher, str(mallory_key), iv))
    print("Mallory's decrypted message (from Bob): ", exchange_message(bob_cipher, str(mallory_key), iv))



if __name__ == "__main__":
    print("\nTASK 2A: key tampering ------------------------------------------------------------------------")
    minm_attack_on_keys()

    print("\nTASK 2B: g = p -----------------------------------------------------------------------------")
    minm_attack_on_g(p=37, g=37)
    print("\nTASK 2B: g = 1 -----------------------------------------------------------------------------")
    minm_attack_on_g(p=37, g=1)
    print("\nTASK 2B: g = p-1 ---------------------------------------------------------------------------")
    minm_attack_on_g(p=37, g=36)

    