from util import xor
from util import hex2base64
hex = "1c0111001f010100061a024b53535009181c"
fixed = "686974207468652062756c6c277320657965"
print(xor(hex.decode("hex"), fixed.decode("hex")).encode("hex"))
