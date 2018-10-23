import collections
import string
from random import SystemRandom

# Public variables here
key = []
cryptotext = []

m = input('Enter the text you wish to encrypt: ')


# Encrypts the message
def encrypt():
    # Initialize local variables here
    k = 0
    rotate_string = m

    # Generates a random int from 0 to 25 for however many chars are in rotate_string
    for i in rotate_string:
        value = SystemRandom().randrange(26)
        key.append(value)  # The key rotates backwards. -value can fix that.

    print(key)

    # Rotates the string by each key value in the list
    for j in rotate_string:
        upper = collections.deque(string.ascii_uppercase)
        lower = collections.deque(string.ascii_lowercase)

        upper.rotate(key[k])
        lower.rotate(key[k])

        upper = ''.join(list(upper))
        lower = ''.join(list(lower))
        r = rotate_string.translate(str.maketrans(string.ascii_uppercase, upper)) \
            .translate(str.maketrans(string.ascii_lowercase, lower))

        # print(list(r)) #Debugging for all the rotated lists

        # Takes one char from each list and creates the cryptotext
        cryptotext.append(r[k])

        # Increments k by 1
        k += 1

    return ''.join(cryptotext)


# Decrypts the message
def decrypt(ncryptotext, nkey):
    o = 0
    mcryptotext = []

    nkey = [-n for n in nkey]
    print(nkey)

    for l in ncryptotext:
        upper = collections.deque(string.ascii_uppercase)
        lower = collections.deque(string.ascii_lowercase)

        upper.rotate(nkey[o])
        lower.rotate(nkey[o])

        upper = ''.join(list(upper))
        lower = ''.join(list(lower))
        ncryptotext = ''.join(ncryptotext)
        r = ncryptotext.translate(str.maketrans(string.ascii_uppercase, upper)) \
            .translate(str.maketrans(string.ascii_lowercase, lower))

        # print(list(r)) #Debugging for all the rotated lists
        ncryptotext = list(ncryptotext)

        # Takes one char from each list and creates the cryptotext
        mcryptotext.append(r[o])
        o += 1

    mcryptotext = ''.join(mcryptotext)
    print(mcryptotext)


print(encrypt())
print(decrypt('Dpmo wuots xgqcfej iezhu!', [16, 18, 22, 4, 1, 23, 13, 20, 20, 14, 8, 8, 2, 23, 24, 6, 7, 15, 11, 14, 10,
                                            18, 3, 24, 24]))
