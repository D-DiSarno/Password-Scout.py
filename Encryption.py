from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def encrypt(message, key):
    cipher = AES.new(key[0:16].encode("utf8"), AES.MODE_ECB)
    to_enc = pad(message.encode("utf-8"), 16)
    result = str(cipher.encrypt(to_enc).hex())
    return result


def decrypt(encrypted, key):
    cipher = AES.new(key[0:16].encode("utf8"), AES.MODE_ECB)
    return unpad(cipher.decrypt(bytes.fromhex(encrypted)), 16).decode("utf-8")
