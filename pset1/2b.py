import itertools
import sys
import re

def read_ciphertexts(filename):
    '''Reads ciphertexts from file and removes spaces'''
    ciphers = open('ciphers.txt', 'r').read()
    ciphers = ciphers.split('\n')[::2]
    return [text.replace(' ', '').decode('hex') for text in ciphers]

def is_int(i):
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

def peel_apart_messages(canceled_pad, charset):
    '''Interactive function for user to guess crib repeatedly
        and make it easy to peel apart two messages'''

    message1 = '_'*len(canceled_pad)
    message2 = '_'*len(canceled_pad)

    while True:
        print 'Current Message 1:'
        print message1
        print 'Current Message 2:'
        print message2

	crib = raw_input("Enter crib: ")
        
        num_positions = len(canceled_pad) - len(crib) + 1
        results = [0]*num_positions
        for i in xrange(num_positions):
            pos_result = str_xor(canceled_pad[i:i+len(crib)], crib)
            results[i] = pos_result
            if re.search(charset, pos_result):
                sys.stdout.write(str(i)+': '+pos_result+'*''\t\t')
            else:
                sys.stdout.write(str(i)+': '+pos_result + '\t\t')
            if i%3 == 0: sys.stdout.write('\n')

	response = raw_input("Enter the position, 'n' for no match, or 'q' to quit: ")
        if response == 'none' or response == 'n':
            print 'No changes made'
        elif is_int(response) and int(response) < num_positions:
            response = int(response)
            one_or_two = raw_input("Is crib part of message 1 or 2? '1' or '2': ")
            if one_or_two == '1':
                message1 = message1[:response] + crib + message1[response+len(crib):]
                print results[response]
                message2 = message2[:response] + results[response] + message2[response+len(crib):]
            elif one_or_two == '2':
                message2 = message2[:response] + crib + message2[response+len(crib):]
                message1 = message1[:response] + results[response] + message1[response+len(crib):]
            else:
                print 'Invalid input!'
        elif response != 'quit' or response != 'q':
            break
        else:
            print 'Invalid input'

ciphertexts = read_ciphertexts('ciphers.txt')
canceled_pad = get_cancelled_pad(ciphertexts)

charset = '^[a-zA-Z0-9.,?! :;\'"]+$'
peel_apart_messages(canceled_pad, charset)


