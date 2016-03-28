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
    assert len(cipher) % 2 == 0
    plaintext = ""
    count = 0
    for cipher_byte in bytes(cipher.decode("hex")):
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
            candidates.append(decrypt(cipher, key))
    return candidates

def score(candidates):
    maxScore = 0
    plaintext = ""
    for candidate in candidates:
        score = englishFreqMatchScore(candidate)
        if (score > maxScore):
            maxScore = score
            plaintext = candidate
    return plaintext

def load(filename):
    with open(filename) as file:
        lines = []
        for line in file:
            lines.append(line.rstrip("\n"))
    return lines

def guessKeysize(filename):
    minDistance = float("inf")
    for keysize in range(2, 40):
        distance = keysizeDistance(filename, keysize)
        if (distance < minDistance):
            minDistance = distance
            predicted = keysize
    return predicted

def keysizeDistance(filename, keysize):
    with open(filename) as file:
        totalDistance = 0.0
        byteCount = 0;
        bytes = file.read(keysize)
        while bytes != "":
            prevBytes = bytes
            bytes = file.read(keysize)
            if (len(bytes) < keysize):
                break
            totalDistance += float(hamming(prevBytes, bytes)) / float(keysize)
            byteCount += 1
    return totalDistance / byteCount

def transpose(filename, keysize):
    with open(filename) as file:
        matrix = [""]*keysize
        print matrix
        bytes = file.read(keysize)#.rstrip("\n")
        while bytes != "":
            for byte_index in range (0, keysize):
                matrix[byte_index] = matrix[byte_index] + bytes[byte_index]
            bytes = file.read(keysize)#.rstrip("\n")
            if (len(bytes) < keysize):
                break
    print matrix
    plaintext = []
    for cipher in matrix:
        #try:
            #print(cipher)
            plaintext.extend(brute(cipher))
        #except:
          #  pass
    print plaintext
    return plaintext
