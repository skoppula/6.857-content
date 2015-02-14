CT1 = 'd2 6b a5 0d 27 6a 34 2d 8e 53 0e'.split(' ')
CT2 = 'de 6e a7 00 30 74 34 2b 8e 51 11'.split(' ')

CT1_num = [int(byte, 16) for byte in CT1]
CT2_num = [int(byte, 16) for byte in CT2]

alphabet = [i+65 for i in range(58)]

PT1 = []
PT2 = []

for i, val in enumerate(CT1_num):
    pad_byte_possibilities = [a^val for a in alphabet]
    print i, pad_byte_possibilities
    
    lst1 = []
    lst2 = []
    for possibility in pad_byte_possibilities:
        temp = possibility ^ CT2_num[i]
        if temp > 64 and temp < 123:
            lst2.append(str(unichr(temp)))
            lst1.append(str(unichr(possibility ^ CT1_num[i])))

    PT2.append(lst2)
    PT1.append(lst1)

print PT1
print PT2

