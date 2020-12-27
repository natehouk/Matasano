from Crypto.Cipher import AES
from util.util import decode_base64
import binascii
import base64

# Given constants
key = "YELLOW SUBMARINE"

# Given input file
filename = "set-1/files/input-7.txt"

# Decrypt file
with open(filename) as file:
    ciphertext = base64.b64decode(file.read().replace("\n", ""))
    print(len(ciphertext))
decobj = AES.new(key, AES.MODE_ECB)
plaintext = decobj.decrypt(ciphertext)

# Print decrypted cipher
print(str(plaintext, "latin-1"))