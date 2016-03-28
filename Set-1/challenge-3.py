from util import brute
from util import score
ciphers = ["1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736".decode("hex")]
print(score(brute(ciphers)))
