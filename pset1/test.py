import re

ciphers_str = open('ciphers.txt', 'r').read().split('\n')[::2]
ciphers = [[int(byte, 16) for byte in cipher.split(' ')] for cipher in ciphers_str]

def xor(xs, ys):
    '''Perform pairwise XOR operation on two lists'''
    return [x ^ y for x, y in zip(xs, ys)]

m = xor(ciphers[0], ciphers[3])

dictionary = open('dictionary', 'r').read().split()
words = set()
for w in dictionary:
    words.add(w)

def commonWords(crib):
    key = [ord(c) for c in crib]
    for i in range(len(m)-len(crib)):
        word = xor(key, m[i:i+len(crib)])
        ascii = "".join([str(unichr(c)) for c in word])
        if all(v is True for v in [c.isalpha() or c.isspace() for c in ascii]):
            print ascii   

common = [' the ', ' there ', ' you ', ' your ', ' he ', ' her ', ' him ', ' she ', ' and ', ' their ', ' like ', ' as ', ' did ', ' said ', ' it ', ' does ', ' not ', ' or ', ' but ', ' if ', ' else ', ' for ', ' let ', ' are ', ' be ', ' to ', ' that ', ' have ', ' on ', ' with ', ' by ', ' from ', ' say ', ' we ', ' will ', ' an ', ' would ', ' what ', ' so ', ' up ', ' out ', ' about ', ' who ', ' get ', ' which ', ' because ', ' go ', ' me ', ' when ', ' can ', ' time ', ' just ', ' know ', ' take ', ' people ', ' into ', ' year ', ' your ', ' good ', ' some ' ]    

for w in common:
    commonWords(w)
