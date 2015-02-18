import itertools

ciphers_str = open('ciphers.txt', 'r').read().split('\n')[::2]
ciphers = [[int(byte, 16) for byte in cipher.split(' ')] for cipher in ciphers_str]

def xor(xs, ys):
    '''Perform pairwise XOR operation on two lists'''
    return [x ^ y for x, y in zip(xs, ys)]

#One of the six combinations will have the pads cancel out.
Xs = dict()
Xs[(0,1)] = xor(ciphers[0], ciphers[1])
Xs[(0,2)] = xor(ciphers[0], ciphers[2])
Xs[(0,3)] = xor(ciphers[0], ciphers[3])
Xs[(1,2)] = xor(ciphers[1], ciphers[2])
Xs[(1,3)] = xor(ciphers[1], ciphers[3])
Xs[(2,3)] = xor(ciphers[2], ciphers[3])

def print_linewrapped(text):
    line_width = 50
    text_len = len(text)
    for chunk in xrange(0,text_len,line_width):
        if chunk > text_len-line_width:
            print str(chunk) + chr(9) + text[chunk:]
        else:
            print str(chunk) + chr(9) + text[chunk:chunk+line_width]

def convert_str(lst):
    return "".join([chr(byte) for byte in lst])

first, second = 0,1
cross = Xs[(first,second)]
m1,m2 = ciphers[first], ciphers[second]
print len(m1)
while response != 'quit':
    print 'Your M1 is', m1
    print 'Your M2 is', m2
    print 'Your cross is', cross
    crib = raw_input('Please enter your crib:')
    crib = [ord(c) for c in crib]
    for index in xrange(len(cross)-len(crib)+1):
        
