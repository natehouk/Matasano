import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Crypto.Cipher import AES
from util.util import xor, pad, encode_hex, xor_bytes, hex2base64
import base64

# Given constants
key = "YELLOW SUBMARINE"
iv = "00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
iv = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
#iv = b'\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41'

# Given input file
filename = "files/input-10a.txt"

# Encrypt file
with open(filename) as file:
    plaintext = file.read().replace("\n", "")

ciphertext = ""
blocks = int(len(plaintext) / 128)
for i in range(0, blocks):
    block = plaintext[i * 128:(i + 1) * 128]
    print(len(block))
    #block = pad(block, 128)
    print(len(block))
    print(block + "$")
    print(str(iv, 'latin-1') + "IV")
    #block = xor(str(block, 'latin-1'), str(iv, 'latin-1'))
    print(str(block) + "#")
    print(len(str(block)))
    #block = pad(block, 128)
    encobj = AES.new(key, AES.MODE_ECB)
    encrypted_block = str(encobj.encrypt(block), 'latin-1')
    ciphertext += encrypted_block
    print(encode_hex(encrypted_block))
    iv = bytes(encrypted_block, 'latin-1')

# Print decrypted cipher
print(hex2base64(encode_hex(ciphertext)))

#091230aade3eb330dbaa4358f88d2a6c37b72d0cf4c22c344aec4142d00ce530b181ceb5742ecf49b495dee7c71cc8ed302b23a133b9d861bece9fa3186610a6195dc11d49044951e80f10593d8fa8cb1bf2dca84330fb55c9a042e0f4592c45128864cd1d0e593467dbe6a63e58b2b776f5b4b1f79fd7a8ccbd3259e99154ae
#091230AADE3EB330DBAA4358F88D2A6C37B72D0CF4C22C344AEC4142D00CE530B181CEB5742ECF49B495DEE7C71CC8ED302B23A133B9D861BECE9FA3186610A6195DC11D49044951E80F10593D8FA8CB1BF2DCA84330FB55C9A042E0F4592C45128864CD1D0E593467DBE6A63E58B2B7D7CBDCAE2D8227780F99FBC504CAFEB2
#091230aade3eb330dbaa4358f88d2a6c37b72d0cf4c22c344aec4142d00ce530b181ceb5742ecf49b495dee7c71cc8ed302b23a133b9d861bece9fa3186610a6195dc11d49044951e80f10593d8fa8cb1bf2dca84330fb55c9a042e0f4592c45128864cd1d0e593467dbe6a63e58b2b77e6c8de0f5ecfca925b725804f45469a