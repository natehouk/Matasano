import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Crypto.Cipher import AES
from util.util import xor, pad, decode_hex, encode_hex
import base64

# Given constants
key = "YELLOW SUBMARINE"
iv = "00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"

# Given input file
filename = "files/input-10a.txt"

# Encrypt file
with open(filename) as file:
    plaintext = file.read().replace("\n", "")
block = plaintext[0:128]
#block = xor(block, iv)
print(block)
encobj = AES.new(key, AES.MODE_ECB)
ciphertext = encobj.encrypt(block)

# Print decrypted cipher
print(encode_hex(str(ciphertext, 'latin-1')))