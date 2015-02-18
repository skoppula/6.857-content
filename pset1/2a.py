CT1_str = 'd2 6b a5 0d 27 6a 34 2d 8e 53 0e'
CT2_str = 'de 6e a7 00 30 74 34 2b 8e 51 11'

CT1 = [int(byte, 16) for byte in CT1_str.split(' ')]
CT2 = [int(byte, 16) for byte in CT2_str.split(' ')]

def xor(xs, ys):
    '''Perform pairwise XOR operation on two lists'''
    return [x ^ y for x, y in zip(xs, ys)]

X = xor(CT1, CT2)

dictionary = open('dictionary', 'r').read().split()
words = set()
for w in dictionary:
    if len(w) == len(X):
        try:
            words.add(w.upper().encode())
        except:
            print 'Problem encoding', w

for PT1_str in words:
    PT1 = [ord(byte) for byte in PT1_str]
    PT2 = xor(PT1, X)
    PT2_str = "".join([chr(byte) for byte in PT2])
    if PT2_str in words:
        pad = xor(PT1, CT1)
        print('PT1 = %s, PT2 = %s, pad = %s' % (PT1_str, PT2_str, pad))
