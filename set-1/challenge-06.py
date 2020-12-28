import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from util.util import hamming, guess_keysize, transpose

# Given test
a = "this is a test"
b = "wokka wokka!!!"
assert(hamming(a, b) == 37)

# Given input file
filename = "files/input-06.txt"

# Guess keysize
keysize = guess_keysize(filename)

# Print keysize
print("Keysize: " + str(keysize[0][1]))

# Print decrypted cipher
print(transpose(filename, keysize[0][1]))