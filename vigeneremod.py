#!/usr/bin/env python3

from Code import *
import copy

key = Code("red")
plain = Code("thequickfoxjumped")

def extended_key(key, length): # length gives number of keys to add
    newkey = key.copy()
    for i in range(length):
        key.add(1)
        newkey.append(key)
    return newkey

extended_key(key,3).print()
