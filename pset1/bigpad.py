ciphers_str = open('ciphers.txt', 'r').read().split('\n')[::2]
cipher = [[int(byte, 16) for byte in cipher.split(' ')] for cipher in ciphers_str]

def xor(xs, ys):
    '''Perform pairwise XOR operation on two lists'''
    return [x ^ y for x, y in zip(xs, ys)]

