import string


def decrypt_data(ciphertext):
    orig = '{' + string.letters + string.digits + '}'
    cipher = "XmQavYuUbsgqAnpZVoCySjrJORBlGTEhPWLNftwciHMDzxFIdKek}{6470513298"
    dec_transl = string.maketrans(cipher, orig)
    result = ciphertext.translate(dec_transl)
    print '[!] Flag:' + result

with open('flag.enc', 'r') as f:
    decrypt_data(f.read())
