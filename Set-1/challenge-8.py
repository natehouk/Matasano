from util import load
from util import detect_aes_ecb
filename = "8.txt"
results = []
for i, line in enumerate(load(filename)):
    detect = detect_aes_ecb(line)
    results.append((detect[0], detect[1], i, line))
results = sorted(results)
x = 0
for r in results:
    if x==0:
        print "%.2f %d %d %s" % (r[0], r[1], r[2], r[3])
    else:
        print "%.2f %d %d" % (r[0], r[1], r[2])
    x += 1
