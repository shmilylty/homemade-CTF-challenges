from random import randint
from math import floor, sqrt

ciphertext = ''
plaintext = '_'
array = [ord(i) for i in plaintext]


key = randint(65, max(array)) * 255
for i in range(len(plaintext)):
    ciphertext += str(int(floor(float(key + array[i]) / 2 + sqrt(key * array[i])) % 255)) + ' '


print ciphertext
