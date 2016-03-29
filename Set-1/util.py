from freq import englishFreqMatchScore

def hex2base64(hex):
    return(hex.decode("hex").encode("base64")[:-1])

def xor(a, b):
    assert len(a) == len(b)
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def hamming(a, b):
    assert len(a) == len(b)
    a = "".join(format(ord(x), '08b') for x in a)
    b = "".join(format(ord(x), '08b') for x in b)
    return sum(x != y for x, y in zip(a, b))

def decrypt(cipher, key):
    plaintext = ""
    count = 0
    for cipher_byte in bytes(cipher):
        index = count % len(key)
        key_byte = bytes(key)[index]
        plaintext = plaintext + xor(cipher_byte, key_byte)
        count += 1
    return plaintext

def encrypt(plaintext, key):
    cipher = ""
    count = 0
    for plaintext_byte in bytes(plaintext):
        index = count % len(key)
        key_byte = bytes(key)[index]
        cipher = cipher + xor(plaintext_byte, key_byte)
        count += 1
    return cipher.encode("hex")

def brute(ciphers):
    candidates = []
    print len(ciphers)

    for cipher in ciphers:
        for i in range(0, 256):
            key = chr(i)
            candidates.append((key, decrypt(cipher, key)))
    #for c in candidates:
    #    print c
    print len(candidates)
    print candidates

    return candidates

def score(candidates):
    results = []

    for candidate in candidates:
        score = englishFreqMatchScore(candidate[1])
        results.append((score, candidate[0], candidate[1]))
    for r in results:
        print r
    #exit()
    results = sorted(results, reverse=True)[:2]
    return results

def load(filename):
    with open(filename) as file:
        lines = []
        for line in file:
            lines.append(line.rstrip("\n").decode("hex"))
    return lines

def guess_keysize(filename):
    with open(filename) as file:
        decoded = bytes(file.read().replace("\n", "").decode("base64"))
        distances = []
        for keysize in range(1, 50):
            distance = average_distance(decoded, keysize)
            distances.append((distance, keysize))
        distances = sorted(distances)
        for x in distances:
            print "%02d %f" % (x[1], x[0])
    return distances

def average_distance(decoded, keysize):
    totalDistance = 0.0
    chunkCount = 0
    chunk = decoded[:keysize]
    while chunk != "":
        prevChunk = chunk
        chunkCount += 1
        chunk = decoded[chunkCount*keysize:chunkCount*keysize+keysize]
        if (len(chunk) == 0 or chunkCount > 4):
            chunkCount -= 1
            break
        totalDistance += float(hamming(prevChunk[:len(chunk)], chunk)) / min(len(chunk), float(keysize))
    return totalDistance / chunkCount

def transpose(filename, keysize):
    with open(filename) as file:
        blocks = {}
        chunkCount = 0
        decoded = bytes(file.read().replace("\n", "").decode("base64"))
        print "------"
        print decoded
        print "------"
        #exit()
        #print keysize
        chunk = decoded[:keysize]
        #print len(chunk)
        #exit()
        while chunk != "":
            for byte_index in range (0, min(len(chunk), keysize)):
                #print byte_index
                print byte_index, chunkCount, keysize, len(chunk), len("B")
                print chunk + "$"
                print chunk[byte_index] + "$"
                print bytes(chunk)[byte_index] + "$"
                #exit()
                blocks[byte_index, chunkCount] = chunk[byte_index]

                #print "!", chunk
                #print "+", blocks[byte_index]
                #print "$", chunk[byte_index]
            print blocks[0,0], blocks[1,0]
            #exit()
            #print blocks[0]

            if (chunkCount > 5):
                pass
                #exit()
            chunkCount += 1
            chunk = decoded[chunkCount*keysize:chunkCount*keysize+keysize]
            if (len(chunk) == 0):
                chunkCount -= 1
                print ("!!!!!")
                #exit()
                break
        print blocks[0,0] + "-" + blocks[1,0]
        print blocks[0,1] + "-" + blocks[1,1]
        print blocks[0,2] + "-" + blocks[1,2]
        print blocks[0,3] + "-" + blocks[1,3]
        print blocks[0,4] + "-" + blocks[1,4]
        print "nate", "nate"
        #exit()
        key = ""
        plaintext = [""]*keysize
        #print "------"
        #print blocks[0]
        #print "------"
        #exit()
        #for x in blocks:
            #print x
        print blocks[0,0]
        print "--------------------E"
        for x in range(0, chunkCount):
            print blocks[0,x]
            print "--"
            if (x>0):
                pass
                #exit()
        #print blocks[1]
        #exit()
        for x in range(0, keysize):
            cipher = ""
            for y in range(0, chunkCount):
                cipher = cipher + blocks[x,y]
            print "------"
            print cipher
            ciphers = [cipher]
            result = score(brute(ciphers))
            print "-------------------------------------"
            for r in result:
                print r

            key = key + result[0][1]
            print len(result)

        #for block_index, block in enumerate(blocks):

        #    if (block_index==0):
        #        print "".join(block)
        #        print "nate"
        #        exit()
        #    ciphers = ["".join(block)]
            #print len(ciphers)
            #exit()


        #    result = score(brute(ciphers))
        #    for r in result:
        #        print r

            #key = key + result[0][1]
            #plaintext[block_index] = result[1]
            #print block_index, "".join(block)
    print "$" + key + "$"
    return decrypt(decoded, key)
