#from http://wiki.birth-online.de/snippets/python/aes-rijndael
from rijndael import rijndael
import os


key_128 = os.urandom(16)
r = rijndael(key_128, block_size = 16)
plaintext = "hello world"
block_adjusted_plaintext = plaintext + (16-len(plaintext))*" "
ciphertext = r.encrypt(block_adjusted_plaintext)
print ciphertext
