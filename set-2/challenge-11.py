import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import random
from util.util import pad, detect_aes_ecb, generate_key, ammend_plaintext, encrypt_random

# Chosen plaintext
plaintext = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

# Generate data and encrypt plaintext
key = generate_key()
plaintext = pad(ammend_plaintext(plaintext), 16)
ciphertext = encrypt_random(key, plaintext)

# Detect AES in ECB mode
detect = detect_aes_ecb(ciphertext)

# Print answer
print("Plaintext: " + str(plaintext, 'latin-1'))
print("Ciphertext: " + str(ciphertext, 'latin-1'))
if (detect[1] == 6):
    print("Guess: ECB without CBC mode")
elif (detect[1] == 4):
    print("Guess: ECB with CBC mode")
else:
    raise Exception