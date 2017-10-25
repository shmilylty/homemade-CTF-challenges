from math import floor, sqrt

with open('flag.enc') as f:
    ciphertext =  list(f.read().strip().split())

for key in xrange(65, 127):
    plaintext = []
    key *= 255
    for j in range(len(ciphertext)):
        for i in range(65, 127):
            if str(int(floor(float(key + i) / 2 + sqrt(key * i)) % 255)) == ciphertext[j]:
                plaintext.append(i)
    if(len(plaintext) == len(ciphertext)):
        print ''.join([chr(k) for k in plaintext])
