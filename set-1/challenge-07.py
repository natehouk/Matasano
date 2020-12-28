from Crypto.Cipher import AES
import base64

# Given constants
key = "YELLOW SUBMARINE"

# Given input file
filename = "files/input-07.txt"

# Decrypt file
with open(filename) as file:
    ciphertext = base64.b64decode(file.read().replace("\n", ""))
decobj = AES.new(key, AES.MODE_ECB)
plaintext = decobj.decrypt(ciphertext)

# Print decrypted cipher
print(str(plaintext, "latin-1"))