from util.util import hamming, guess_keysize, transpose, score

# Given test
a = "this is a test"
b = "wokka wokka!!!"
assert(hamming(a, b) == 37)

# Given input file
filename = "set-1/files/input-6.txt"

# Guess keysize
keysize = guess_keysize(filename)

# Print keysize
print("Keysize: " + str(keysize[0][1]))

# Print decrypted cipher
print(transpose(filename, keysize[0][1]))