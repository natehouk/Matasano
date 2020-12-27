from util.util import brute, score, decode_hex

# Given constants
ciphers = [decode_hex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")]

# Brute force ciphers and rank by score
max = 0
for score in score(brute(ciphers)):

    # Update highest scoring cipher
    if(score[0] > max):
        high_score = score
        max = score[0]

# Print high score message
print(high_score[2])