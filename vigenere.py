#!/usr/bin/env python3
import numpy as np

cipher = "DCSTUZAVBABCJDNLFALEDECGFLHHTEOHZZZXFNBRJBOITQIVTPWYSPWSNXORJNUXJZHMOEBIQCYWFYWIPQUHWPLWBCCEMMYLBGCSSXIVFRYRFCUPMJWVZANSHCUTIJCWBMIYUNIRTELYDECRHLHHBYUPZKCRHALSUZWSMDNLBEJVFGYRUEBMSOJESECITZLXIPJYCWCGGCIQSPUHJYATSTPEUPGITDUKFDGSEPLRDCSTUZAVBABCFICWUDUXUSYMOEYVTPWXJZHSGEBIETMGJAFMOPMSGXUXIPGEUTWWDZGTVEYVTNCIONYMOQIVNLNMPYMIDFLMUJYPFNNVJNUPFYAMOPYVJYAHJRCXBWMMHYUPQCIGFDMMORJLZDCGTLHHPEBISDWSSPWSONYTUDLIMLNIEEIMOQIVNLNMPYMIDFLMUJXEULWSOQCHFYNMBWCXZOUXBTHXFRLMUJUYUSYRUTWEUTIRBYXRPYLIQFXMBECSOLLIBWMSDPHXSLFXPNLCQEIKSLJLZALEDECGBWUTQWCGBECSODIJDCSTUZAVBABCJYWPVOYIMPWXSZHMDNIQNPLGFNBMQMUWFOJEZXYRUNUVEDXMHTNEMNOVSPHGJPMGPXJYUPLTBDMAPCXWBYXQJWCXBCSGPXGYOTWEUTIRTNLCQEIKSLJLZALMPCNSUSYQPOYVOLAIXLMIGQYGUTPIMJMCOZHCNZOWXTNLFYWVZANMPYWSOGYVUTHKSPUHBMFIJYZSSXUXJZHTMLCRUPRXUZORJYNIMWCKJMFIOZHWFYMIUPRXDTJLFCNIYEQLJNBGBYIRMJVISPUHCJLIWPLWJYAXIPJVPNYWTOYGSJJXJZHXIPMIOOYVPQURFYWVZANIENIHFOGITDUKFDBESPMXIPXIDCSTUTIREPWSETHKUPWLO"

indices = [index for index in range(len(cipher)) if cipher.startswith("DCSTU",index)]
print(indices)
# [0, 232, 544, 900]

print(np.gcd(544-232, 900 - 544))
# 4

def iOC(string):
    n = len(string)
    total = 0
    for let in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        total += string.count(let)**2 / n**2
    return total

def toNumeric(string):
    numbers = []
    lets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in string:
        numbers.append(lets.index(i))

    return numbers

def toText(numbers):
    string = ""
    lets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in numbers:
        string = string + lets[i]

    return string

y = ["","","",""]
for i in range(len(cipher)):
    y[i % 4] = y[i % 4] + cipher[i]


def shiftCipher(string,key): #decrypt shift
    plain = toNumeric(string)
    key_num = toNumeric(key)[0]
    cipher = []
    for i in plain:
        cipher.append((i - key_num) % 26)
    cipherText = toText(cipher)
    return cipherText
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

def mG(text,g):
    n = len(text)
    total = 0
    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        p_i = P(toNumeric(i)[0])
        f_i = text.count(toText([(toNumeric(i)[0] + g) % 26]))
        total += p_i * f_i / n
    return total

for g in range(26):
    print(g, ": ", mG(y[3],g))

# BLUE

key = "BLUE"
p = []
for i in range(len(key)):
   p.append(shiftCipher(y[i],key[i]))

plain = ""
for i in range(len(cipher)):
    plain += p[i % 4][i // 4]
print(plain)
