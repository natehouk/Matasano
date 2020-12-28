import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from util.util import score, load, brute

# Given input file
filename = "files/input-04.txt"

# Brute force ciphers and rank by score
max = 0
for score in score(brute(load(filename))):

    # Update highest scoring cipher
    if(score[0] > max):
        high_score = score
        max = score[0]

# Print high score message
print(high_score[2])