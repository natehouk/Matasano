from util import hamming
from util import guess_keysize
from util import transpose
from util import score
a = "this is a test"
b = "wokka wokka!!!"
print(hamming(a, b))
filename = "6.txt"
keysize = guess_keysize(filename)
print("Keysize: " + str(keysize))
print(transpose(filename, keysize))
