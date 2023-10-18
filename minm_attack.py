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

    alice_cipher = create_cipher(pad(b"hi bob", BLOCK_SIZE), str(alice_key), iv)
    bob_cipher = create_cipher(pad(b"hi alice", BLOCK_SIZE), str(bob_key), iv)

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

    alice_cipher = create_cipher(pad(b"hi bob", BLOCK_SIZE), str(alice_key), iv)
    bob_cipher = create_cipher(pad(b"hi alice", BLOCK_SIZE), str(bob_key), iv)

    print("Alice's cipher:", alice_cipher)
    print("Bob's cipher:", bob_cipher)
    print("Bob's decrypted message: ", exchange_message(bob_cipher, str(bob_key), iv))
    print("Alice's decrypted message: ", exchange_message(alice_cipher, str(alice_key), iv))

    if p == g:
        h = SHA256.new(data = bytes(str(0).encode("utf8")))
    elif g == 1:
        h = SHA256.new(data = bytes(str(1).encode("utf8")))
    elif g == p-1:
        if (alice_a % 2 == 0):
            h = SHA256.new(data = bytes(str(1).encode("utf8")))
        else:
            h = SHA256.new(data = bytes(str(p-1).encode("utf8")))
    mallory_key = bin(int(h.hexdigest(),16))[2:18]
    print("mallory's key", mallory_key)
    print("alice's key", alice_key)
    print("bob's key", bob_key)
    print("Mallory's decrypted message (from Alice): ", exchange_message(alice_cipher, str(mallory_key), iv))
    print("Mallory's decrypted message (from Bob): ", exchange_message(bob_cipher, str(mallory_key), iv))



if __name__ == "__main__":
    print("\nTASK 2A: key tampering ------------------------------------------------------------------------")
    minm_attack_on_keys()
    p = formatHex("B10B8F96 A080E01D DE92DE5E AE5D54EC 52C99FBC FB06A3C6 9A6A9DCA 52D23B61 6073E286 75A23D18 9838EF1E 2EE652C0 13ECB4AE A9061123 24975C3C D49B83BF ACCBDD7D 90C4BD70 98488E9C 219A7372 4EFFD6FA E5644738 FAA31A4F F55BCCC0 A151AF5F 0DC8B4BD 45BF37DF 365C1A65 E68CFDA7 6D4DA708 DF1FB2BC 2E4A4371")

    print("\nTASK 2B: g = p -----------------------------------------------------------------------------")
    g = p
    minm_attack_on_g(p, g)
    print("\nTASK 2B: g = 1 -----------------------------------------------------------------------------")
    minm_attack_on_g(p, g=1)
    print("\nTASK 2B: g = p-1 ---------------------------------------------------------------------------")
    g = p - 1
    minm_attack_on_g(p, g)

    