#!/usr/bin/env python3

from Code import *
import copy

key = Code("red")
plain = Code("thequickfoxjumped")
ciphertext = "IYMYSILONRFNCQXQJEDSHBUIBCJUZBOLFQYSCHATPEQGQJEJNGNXZWHHGWFSUKULJQACZKKJOAAHGKEMTAFGMKVRDOPXNEHEKZNKFSKIFRQVHHOVXINPHMRTJPYWQGJWPUUVKFPOAWPMRKKQZWLQDYAZDRMLPBJKJOBWIWPSEPVVQMBCRYVCRUZAAOUMBCHDAGDIEMSZFZHALIGKEMJJFPCIWKRMLMPINAYOFIREAOLDTHITDVRMSE".lower()
cipher = Code(ciphertext)

def extended_key(key, length): # length gives number of keys to add
    newkey = key.copy()
    rkey = key.copy()
    for i in range(length):
        rkey.add(1)
        newkey.append(rkey)
    return newkey

def encrypt(plain,key):
    pt = plain.copy() #always make copy
    length = len(plain.code) // len(key.code) + 1
    extkey = extended_key(key,length)
    return pt.add_code(extkey)

def decrypt(cipher,key):
    ct = cipher.copy() #always make copy
    length = len(ct.code) // len(key.code) + 1
    extkey = extended_key(key,length)
    extkey.scale(-1) # subtract to decrypt
    return ct.add_code(extkey)

#cipher = encrypt(plain,key)
#cipher.print()

#ptest = decrypt(cipher,key)
#ptest.print()
def findIndexes(cipher, text):
    for i in range(15):
        try:
            index = cipher.text().index(text.text())
        except:
            print("not found")
        print(index)
        text.add(1)
        text.print()
    
print(np.gcd(87,167))    

for i in range(len(ciphertext) - 3):
    text = ciphertext[i:i+3]
    findIndexes(cipher,Code(text))

# 50, 65
# 70, 105
decrypt(cipher,Code("prime")).print()