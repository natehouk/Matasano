import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from util.util import encrypt_xor

# Given encryption key
key = "ICE"

# Given text to encrypt
plaintext = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"

# Print encrypted text
print(str(encrypt_xor(plaintext, key), "latin-1"))