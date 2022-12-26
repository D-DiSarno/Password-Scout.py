import hashlib
def hash_String(message):
    hashed_string = hashlib.sha256(message.encode('utf-8')).hexdigest()
    print(hashed_string)
    return hashed_string