import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from util.util import decrypt_ecb
import base64

# Given constants
key = "YELLOW SUBMARINE"

# Given input file
filename = "files/input-07.txt"

# Decrypt file
with open(filename) as file:
    ciphertext = base64.b64decode(file.read().replace("\n", ""))
plaintext = decrypt_ecb(key, ciphertext)

# Print decrypted cipher
print(str(plaintext, "latin-1"))