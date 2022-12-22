from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def encrypt(message, key):
    cipher = AES.new(key, AES.MODE_ECB)
    message = pad(message, 16)
    return cipher.encrypt(message)


def decrypt(encrypted, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return unpad(cipher.decrypt(encrypted), 16)
