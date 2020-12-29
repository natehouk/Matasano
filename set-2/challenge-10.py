import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Crypto.Cipher import AES
from util.util import xor, pad, bytes2hex, encode_hex, encrypt_ecb, decrypt_ecb, decrypt_ecb_with_cbc, encrypt_ecb_with_cbc
import base64

# Given constants
key = b"YELLOW SUBMARINE"
iv = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

# Given input file
filename = "files/input-10a.txt"

# Open file and read plaintext
with open(filename) as file:
    plaintext = file.read().replace("\n", "")

# Encrypt plaintext using ECB in CBD mode using given key
ciphertext = encrypt_ecb_with_cbc(plaintext, key, iv)
print(bytes2hex(ciphertext))

# Decrypt ciphertext using ECB in CBC mode using given key
print(decrypt_ecb_with_cbc(ciphertext, key, iv))