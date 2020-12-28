import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from util.util import xor, decode_hex, encode_hex

# Given constants
hex = "1c0111001f010100061a024b53535009181c"
fixed = "686974207468652062756c6c277320657965"

# Decode given strings into hex
decoded_hex = decode_hex(hex)
decoded_fixed = decode_hex(fixed)

# Perform xor operation over hex values
xor_value = xor(decoded_hex, decoded_fixed)

# Encode back into hex
hex_value = encode_hex(xor_value)

# Print answer
print(str(hex_value, "latin-1"))