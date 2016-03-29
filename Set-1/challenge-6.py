from util import hamming
from util import guess_keysize
from util import transpose
from util import score
a = "this is a test"
b = "wokka wokka!!!"
print(hamming(a, b))
filename = "6.txt"
keysize = guess_keysize(filename)
print("Keysize Scores: " + str(keysize))
print("Keysize: " + str(keysize[0][1]))
print(transpose(filename, keysize[0][1]))
