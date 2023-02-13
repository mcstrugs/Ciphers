#!/usr/bin/env python3

from Code import *
import copy

key = Code("red")
plain = Code("thequickfoxjumped")

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
    extkey.scale(-1)
    return ct.add_code(extkey)

cipher = encrypt(plain,key)
cipher.print()

ptest = decrypt(cipher,key)
ptest.print()
