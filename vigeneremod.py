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

def P(i):
    mydict = {
        0: 0.082,
        1: 0.015,
        2: 0.028,
        3: 0.043,
        4: 0.127,
        5: 0.022,
        6: 0.020,
        7: 0.061,
        8: 0.070,
        9: 0.002,
        10: 0.008,
        11: 0.040,
        12: 0.024,
        13: 0.067,
        14: 0.075,
        15: 0.019,
        16: 0.001,
        17: 0.060,
        18: 0.063,
        19: 0.091,
        20: 0.028,
        21: 0.010,
        22: 0.023,
        23: 0.001,
        24: 0.020,
        25: 0.001,
    }
    return mydict[i]
    
print(np.gcd(87,167))    

#for i in range(len(ciphertext) - 3):
#    text = ciphertext[i:i+3]
#    findIndexes(cipher,Code(text))

y = ["","","","",""]
for i in range(len(ciphertext)):
    y[i % 5] = y[i % 5] + ciphertext[i]

my_code = Code(y[4])
for i in range(len(my_code.code)):
    my_code.code[i] -= i
    my_code.code[i] = my_code.code[i] % 26

def mG(my_code,g):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    text = my_code.text()
    n = len(text)
    total = 0
    for i in range(26):
        p_i = P(i)
        f_i = text.count(alpha[(i + g) % 26])
        total += p_i * f_i / n
    return total

#def mG(text,g):
#    n = len(text)
#    total = 0
#    for i in range(26):
#        p_i = P(i)
#        f_i = text.count(toText([(toNumeric(i)[0] + g) % 26]))
#        total += p_i * f_i / n
#    return total

for g in range(26):
    print(g, ": ", mG(my_code,g))

# 15,17,8,12,4

print(toText([15,17,8,12,4]))
# 'prime'

# 50, 65
# 70, 105
decrypt(cipher,Code("prime")).print()