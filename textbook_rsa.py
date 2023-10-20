# Task 3
from Crypto.Util.number import getPrime
from binascii import hexlify
from minm_attack import *


#calculates the inverse of a number mod n
def inverse(a,n) :
   t = 0
   r = n
   new_t = 1
   new_r = a
   while (new_r != 0) :
       quotient = r/new_r
       (t,new_t) = (new_t, t - (quotient * new_t))
       (r, new_r) = (new_r, r - (quotient * new_r))
   if (r > 1) :
         return "a is not invertible"
   if (t < 0) :
      t = t + n
   return t

def RSA_encrypt(m,e,n):
   return pow(m,e,n)

def RSA_decrypt(c,d,n):
    return pow(c,d,n)

def textbook_rsa():
   e = 65537                #2^16 + 1
   #Alice public key
   p = getPrime(512)
   q = getPrime(512)   
   n = p * q
   phi = (p-1)*(q-1)
   m =  "hello angelika"
   print("original msg:", m)
   m = int(hexlify(b"hello angelika"), 16)
   encrypted_msg = RSA_encrypt(m,e,n)
   d = pow(e, -1, phi)

   decrypted_msg = hex(RSA_decrypt(encrypted_msg,d,n))[2:]
   msg = bytes.fromhex(decrypted_msg).decode('utf-8')
   print("Decoded msg: ", msg)

def textbook_rsa_attack():
   e = 65537
   p = getPrime(512)
   q = getPrime(512)   
   n = p * q
   phi = (p-1)*(q-1)

   bob_s = 13
   c = RSA_encrypt(bob_s,e,n)
   print("Bob's original cipher:", c)

   # f(c) mallebility attack starts here
   mallory_m = 333
   print("mallory's mallebility attack:", mallory_m)
   c = pow((mallory_m), e, n)
   
   d = pow(e, -1, phi)
   alice_s = RSA_decrypt(c, d, n)
   print("decrypted tampered message:", alice_s)
   

if __name__ == "__main__":
   textbook_rsa()
   print("-----------------------------------------------------------------------------")
   textbook_rsa_attack()