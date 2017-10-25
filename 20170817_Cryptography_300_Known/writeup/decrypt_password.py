from base64 import b64decode
from Crypto.Util.strxor import strxor

def decrypt_data(ciphertext):
    cipher = "JFK63wT1zksfFnACSd93c5WzN5PURZNH"
    print '[!] Cipher:' + cipher
    plaintext = strxor(b64decode(ciphertext), cipher)
    return plaintext

with open("password.enc", 'r') as f:
    print '[!] Password:' + decrypt_data(f.read())
