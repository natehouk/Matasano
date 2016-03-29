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
print(transpose(filename, 2))
raw_input("Press Enter to continue...")
print(transpose(filename, 5))
raw_input("Press Enter to continue...")
print(transpose(filename, 18))
raw_input("Press Enter to continue...")
print(transpose(filename, 29))
raw_input("Press Enter to continue...")
