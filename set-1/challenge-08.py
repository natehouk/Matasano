from util.util import load, encode_hex, detect_aes_ecb

# Given input file
filename = "set-1/files/input-8.txt"

# Enumerate encrypted texts
results = []
for i, line in enumerate(load(filename)):

    # Detect AES in ECB mode
    detect = detect_aes_ecb(line)
    results.append((detect[0], detect[1], i, line))

# Find most likely candidate
results = sorted(results)

# Print answer
print(str(encode_hex(results[0][3]), 'latin-1'))