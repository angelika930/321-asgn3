# Task 1
# Answers Document: https://docs.google.com/document/d/19QCwZsk8nNX-VQG5AtfAyo1RBUetRGGEkAW0fyaeEbQ/edit?usp=sharing
# pip install pycryptodome

from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from random import randint
from Crypto.Hash import SHA256

BLOCK_SIZE = 16         # 128 bits


def noSpace(input: hex) :
    input = input.replace(" ", "").replace("\n", "")
    input = int(input, 16)
    return input

        
def calc_key(p: int,g: int, a:int) -> int :      #p and g comes from sender
    val = g**(a)
    return val % p

def key_exchange(their_value: int, my_int: int, p:int) -> hex: #A is calculated by opposite party
    shared_key = bytes((their_value**my_int)%p)
    h = SHA256.new(data = shared_key)
    return h.hexdigest()

def create_cipher(message: bytes, key: str, iv: bytes) -> bytes:
    cipher = AES.new(key.encode("utf8"), AES.MODE_CBC, iv)
    cipher_text = cipher.encrypt(message)
    return cipher_text

def exchange_message(message: bytes, key:str, iv: bytes) -> bytes: #takes in the encrypted message
    cipher = AES.new(key.encode("utf8"), AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(message)
    decrypted = unpad(decrypted, BLOCK_SIZE)
    return decrypted

if __name__ == "__main__":
    p = 37
    g = 5

    # p = noSpace("B10B8F96 A080E01D DE92DE5E AE5D54EC 52C99FBC FB06A3C6 9A6A9DCA 52D23B61 6073E286 75A23D18 9838EF1E 2EE652C0 13ECB4AE A9061123 24975C3C D49B83BF ACCBDD7D 90C4BD70 98488E9C 219A7372 4EFFD6FA E5644738 FAA31A4F F55BCCC0 A151AF5F 0DC8B4BD 45BF37DF 365C1A65 E68CFDA7 6D4DA708 DF1FB2BC 2E4A4371")
    # g = noSpace("A4D1CBD5 C3FD3412 6765A442 EFB99905 F8104DD2 58AC507F D6406CFF 14266D31 266FEA1E 5C41564B 777E690F 5504F213 160217B4 B01B886A 5E91547F 9E2749F4 D7FBD7D3 B9A92EE1 909D0D22 63F80A76 A6A24C08 7A091F53 1DBF0A01 69B6A28A D662A4D1 8E73AFA3 2D779D59 18D08BC8 858F4DCE F97C2A24 855E6EEB 22B3B2E5")

    iv = get_random_bytes(16)
    alice_a = randint(1, p-2)
    alice = calc_key(p, g, alice_a)
    bob_b = randint(1, p-2)
    bob = calc_key(p, g, bob_b)

    alice_key = bin(int(key_exchange(bob, alice_a, p), 16))[2:18]
    bob_key = bin(int(key_exchange(alice, bob_b, p),16))[2:18]

    alice_key = bin(44885
    bob_key = 1010111101010101

    print("Alice's key:", alice_key)
    print("Bob's key:", bob_key)
    print("Same?", alice_key == bob_key)
    print("Alice's cipher:", create_cipher(pad(b"hi bob", 16), str(alice_key), iv))
    print("Bob's cipher:", create_cipher(pad(b"hi alice", 16), str(bob_key), iv))

    a_msg = create_cipher(pad(b"hi bob", 16), str(alice_key), iv)
    b_msg = create_cipher(pad(b"hi alice", 16), str(bob_key), iv)
    print("Bob's decrypted message: ", exchange_message(b_msg, str(bob_key), iv))
    print("Alice's decrypted message: ", exchange_message(a_msg, str(alice_key), iv))

    