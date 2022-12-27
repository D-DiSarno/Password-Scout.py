import hashlib


def hash_string(message):
    hashed_string = hashlib.sha256(message.encode('utf-8')).hexdigest()
    return hashed_string
