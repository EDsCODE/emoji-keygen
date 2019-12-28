import random
from Crypto.Hash import keccak


def generate_new_address():
    hash = random.getrandbits(256)
    return hex(hash)


def encrypt(address):
    normalized_address = normalize(address)
    keccak_hash = keccak.new(digest_bits=384)
    keccak_hash.update(normalized_address.encode("utf8"))
    return keccak_hash.hexdigest()


def normalize(address):
    return address.lower().replace('0x', '')
