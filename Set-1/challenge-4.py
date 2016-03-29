from util import score
from util import load
from util import brute
filename = "4.txt"
for score in score(brute(load(filename))):
    print score
