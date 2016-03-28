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
    for cipher in ciphers:
        for i in range(0, 256):
            key = chr(i)
            candidates.append((key, decrypt(cipher, key)))
    return candidates

def score(candidates):
    maxScore = 0
    plaintext = ""
    for candidate in candidates:
        score = englishFreqMatchScore(candidate[1])
        if (score > maxScore):
            maxScore = score
            key = candidate[0]
            plaintext = candidate[1]
    return (key, plaintext)

def load(filename):
    with open(filename) as file:
        lines = []
        for line in file:
            lines.append(line.rstrip("\n").decode("hex"))
    return lines

def guess_keysize(filename):
    minDistance = float("inf")
    for keysize in range(1, 40):
        distance = average_distance(filename, keysize)
        print keysize, distance
        if (distance < minDistance):
            minDistance = distance
            predicted = keysize
    return predicted

def average_distance(filename, keysize):
    with open(filename) as file:
        totalDistance = 0.0
        chunkCount = 0
        decoded = bytes(file.read().replace("\n", "").decode("base64"))
        chunk = decoded[:keysize]
        while chunk != "":
            prevChunk = chunk
            chunkCount += 1
            chunk = decoded[chunkCount*keysize:chunkCount*keysize+keysize]
            if (len(chunk) == 0):
                break
            totalDistance += float(hamming(prevChunk[:len(chunk)], chunk)) / float(min(len(chunk), keysize))
    return totalDistance / chunkCount

def transpose(filename, keysize):
    print keysize
    with open(filename) as file:
        blocks = [""]*keysize
        chunkCount = 0
        decoded = bytes(file.read().replace("\n", "").decode("base64"))
        chunk = decoded[:keysize]
        while chunk != "":
            #print chunk.encode("hex")
            #print len(chunk)
            #exit()
            for byte_index in range (0, min(len(chunk), keysize)):
                blocks[byte_index] = blocks[byte_index] + chunk[byte_index]
            chunkCount +=1
            chunk = decoded[chunkCount*keysize:chunkCount*keysize+keysize]
        key = ""
        plaintext = [""]*keysize
        for block_index, block in enumerate(blocks):
            result = score(brute(block))
            print result
            key = key + result[0]
            plaintext[block_index] = result[1]
    print decoded
    print key
    return decrypt(decoded, key)
