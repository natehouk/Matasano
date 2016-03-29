from Crypto.Cipher import AES
import binascii
key = "YELLOW SUBMARINE"
filename = "7.txt"
with open(filename) as file:
    ciphertext = file.read().replace("\n", "").decode("base64")
decobj = AES.new(key, AES.MODE_ECB)
plaintext = decobj.decrypt(ciphertext)
print plaintext
