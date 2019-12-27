import random
import bcrypt


def generate_new_address():
    hash = random.getrandbits(256)
    return hex(hash)


def encrypt(address):
    normalized_address = normalize(address)
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(normalized_address.encode(), salt)
    return hashed.decode()


def normalize(address):
    return address.lower().replace('0x', '')
