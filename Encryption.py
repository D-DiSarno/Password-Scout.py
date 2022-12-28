from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def encrypt(message, key):
    cipher = AES.new(key[0:16].encode("utf8"), AES.MODE_ECB)
    message = pad(message.encode("utf-8"), 16)
    return cipher.encrypt(message)


def decrypt(encrypted, key):
    cipher = AES.new(key[0:16].encode("utf8"), AES.MODE_ECB)
    return unpad(cipher.decrypt(encrypted), 16)
