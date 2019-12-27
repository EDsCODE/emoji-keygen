import random

emojis = ['\\U0001F600',
          '\\U0001F603',
          '\\U0001F604',
          '\\U0001F601',
          '\\U0001F606',
          '\\U0001F605',
          '\\U0001F923',
          '\\U0001F602',
          '\\U0001F642',
          '\\U0001F643',
          '\\U0001F609',
          '\\U0001F60A',
          '\\U0001F607',
          '\\U0001F60D',
          '\\U0001F618',
          '\\U0001F617',
          '\\U0001F61A',
          '\\U0001F619',
          '\\U0001F60B',
          '\\U0001F61C',
          '\\U0001F92A',
          '\\U0001F61D',
          '\\U0001F911',
          '\\U0001F917',
          '\\U0001F92D',
          '\\U0001F92B',
          '\\U0001F922',
          '\\U0001F910',
          '\\U0001F929',
          ]

BASE = 29

# Convert a decimal to a number in BASE


def to_new_base(n):
    separated = []
    while n:
        separated.append(int(n % BASE))
        n //= BASE
    reversed = separated[::-1]
    return reversed

# Convert a number in BASE to decimal


def to_base10(seq):
    reversed = seq[::-1]
    total = 0

    for i, v in enumerate(reversed):
        total += v * (BASE ** i)
    return total

# Using the array of emoji codes provided map a sequence of numbers (BASE = 29) to emojis


def convert_to_emojis(seq):
    result = ""
    for i in seq:
        s = emojis[i].encode('ASCII').decode('unicode-escape')
        result += s
    return result

# Convert emojis to sequence of numbers using the provided emoji array


def emojis_to_base(emoji_str):
    inverted_emoji_dict = {
        v.encode("ASCII").decode('unicode-escape'): i for i, v in enumerate(emojis)}
    result = []
    for i, v in enumerate(emoji_str):
        s = inverted_emoji_dict[v]
        result.append(s)
    return result


def encode(addr):
    dec_rep = int(addr, 0)
    new_base29 = to_new_base(
        dec_rep)
    return convert_to_emojis(new_base29)


def decode(emojis):
    unemojified = emojis_to_base(emojis)
    new_base10 = to_base10(unemojified)
    return hex(new_base10)


# generate a hex and run it through entire stack of encoding and decoding
def test():
    example_hex = hex(random.getrandbits(256))
    new_int = int(example_hex, 0)
    print(new_int)
    new_base29 = to_new_base(
        new_int)
    print(new_base29)
    emojified = convert_to_emojis(new_base29)
    unemojified = emojis_to_base(emojified)
    print(unemojified)
    new_base10 = to_base10(unemojified)
    print(new_base10)
    new_hex = hex(new_base10)
