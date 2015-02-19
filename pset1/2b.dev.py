import itertools
import sys
import re

def read_ciphertexts(filename):
    '''Reads ciphertexts from file and removes spaces'''
    ciphers = open(filename, 'r').read()
    ciphers = ciphers.split('\n')[::2]
    return [text.replace(' ', '').decode('hex') for text in ciphers]

def get_dictionary_words(filename):
    '''Read dictionary file and returns set of words'''
    dictionary = open(filename).read()
    return set(dictionary.split('\n'))

def is_int(i):
    '''Tests if variable is valid integer value'''
    try:
        int(i)
        return True
    except ValueError:
        return False

def str_xor(str1, str2):
    '''Perform pairwise XOR operation on two strings'''
    return ''.join(chr(ord(x) ^ ord(y)) for x,y in zip(str1,str2))

def get_cancelled_pad(ciphertexts):
    '''Performs pairwise XOR's between ciphertexts
    and determines which cross has the pad canceled out
    by frequency of zeroes'''

    best_i, best_j, best_freq = 0, 0, 0
    for i, text1 in enumerate(ciphertexts):
        for j, text2 in enumerate(ciphertexts):
            if i == j: continue
            count = sum([1 if c == '0' else 0 for c in str_xor(text1, text2).encode('hex')])
            if count > best_freq:
                best_i, best_j, best_freq = i, j, count

    print 'Using ciphertext cross with', best_i, 'and', best_j
    return str_xor(ciphertexts[best_i], ciphertexts[best_j])

def auto_peel_apart_messages(canceled_pad, charset, dictionary):
    
    fdictionary = set([' ' + word.upper() + ' ' for word in dictionary if len(word) > 2])
    big_words = [word for word in dictionary if len(word) > 4]

    print 'Total size of enumeration', len(big_words)
    for i, word in enumerate(big_words):
        if i%100 == 0: print i
	crib = word
        
        num_positions = len(canceled_pad) - len(crib) + 1
        for i in xrange(num_positions):
            pos_result = ' ' + str_xor(canceled_pad[i:i+len(crib)], crib) + ' '
            search = pos_result.upper()
            if re.search(charset, pos_result) and any([w in search for w in fdictionary]):
                print i, crib, pos_result

ciphertexts = read_ciphertexts('ciphers.txt')
canceled_pad = get_cancelled_pad(ciphertexts)

#charset = '^[a-zA-Z0-9.,?! :;\'"]+$'
charset = '^[a-zA-Z0-9., ;"]+$'
dictionary = get_dictionary_words('dictionary')
auto_peel_apart_messages(canceled_pad, charset, dictionary)

