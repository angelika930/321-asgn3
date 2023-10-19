# Task 3
from Crypto.Util.number import getPrime
import random

#calculates the inverse of a number mod n
def inverse(a,n) :
   t = 0
   r = n
   new_t = 1
   new_r = a
   while (new_r != 0) :
       quotient = r/new_r
       (t,new_t) = (new_t, t - quotient * new_t)
       (r, new_r) = (new_r, r - quotient * new_r)
   if (r > 1) :
         return "a is not invertible"
   if (t < 0) :
      t = t + n
   return t



    

if __name__ == "__main__":
    #Alice public key
    alice_p = getPrime(512)
    alice_q = getPrime(512)
    alice_n = alice_p * alice_q
    alice_theta = (alice_p-1)*(alice_q-1)

   #Bob public key
    bob_p = getPrime(512)
    bob_q = getPrime(512)
    bob_n = bob_p * bob_q
    bob_theta = (bob_p-1)*(bob_q-1)




