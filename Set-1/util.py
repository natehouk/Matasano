def hamming(a, b):
    assert len(a) == len(b)
    a = "".join(format(ord(x), '08b') for x in a)
    b = "".join(format(ord(x), '08b') for x in b)
    return sum(x != y for x, y in zip(a, b))

def hex2base64(hex):
    return(hex.decode("hex").encode("base64")[:-1])

def xor(a, b):
    assert len(a) == len(b)
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def decrypt(cipher, key):
    plaintext = ""
    count = 0
    print "$" + cipher
    print "NA"
    print bytes(cipher)
    print len(cipher)
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

def brute(cipher):
    plaintext = []
    for i in range(0, 256):
        key = chr(i)
        plaintext.append(decrypt(cipher, key))
    return plaintext

def rank(english):
    maxScore = 0
    plaintext = ""
    for candidate in english:
        score = englishFreqMatchScore(candidate)
        if (score > maxScore):
            maxScore = score 
            plaintext = candidate
    return plaintext

def crack(filename):
    with open(filename) as file:
        plaintext = []
        for line in file:
            try:
                plaintext.extend(brute(line[:-1]))
            except: 
                pass
    return plaintext

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

# Frequency Finder
# http://inventwithpython.com/hacking (BSD Licensed)

# frequency taken from http://en.wikipedia.org/wiki/Letter_frequency
englishLetterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}
ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def getLetterCount(message):
    # Returns a dictionary with keys of single letters and values of the
    # count of how many times they appear in the message parameter.
    letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

    for letter in message.upper():
        if letter in LETTERS:
            letterCount[letter] += 1

    return letterCount

def getItemAtIndexZero(x):
    return x[0]

def getFrequencyOrder(message):
    # Returns a string of the alphabet letters arranged in order of most
    # frequently occurring in the message parameter.

    # first, get a dictionary of each letter and its frequency count
    letterToFreq = getLetterCount(message)

    # second, make a dictionary of each frequency count to each letter(s)
    # with that frequency
    freqToLetter = {}
    for letter in LETTERS:
        if letterToFreq[letter] not in freqToLetter:
            freqToLetter[letterToFreq[letter]] = [letter]
        else:
            freqToLetter[letterToFreq[letter]].append(letter)

    # third, put each list of letters in reverse "ETAOIN" order, and then
    # convert it to a string
    for freq in freqToLetter:
        freqToLetter[freq].sort(key=ETAOIN.find, reverse=True)
        freqToLetter[freq] = ''.join(freqToLetter[freq])

    # fourth, convert the freqToLetter dictionary to a list of tuple
    # pairs (key, value), then sort them
    freqPairs = list(freqToLetter.items())
    freqPairs.sort(key=getItemAtIndexZero, reverse=True)

    # fifth, now that the letters are ordered by frequency, extract all
    # the letters for the final string
    freqOrder = []
    for freqPair in freqPairs:
        freqOrder.append(freqPair[1])

    return ''.join(freqOrder)

def englishFreqMatchScore(message):
    # Return the number of matches that the string in the message
    # parameter has when its letter frequency is compared to English
    # letter frequency. A "match" is how many of its six most frequent
    # and six least frequent letters is among the six most frequent and
    # six least frequent letters for English.
    freqOrder = getFrequencyOrder(message)

    matchScore = 0
    # Find how many matches for the six most common letters there are.
    for commonLetter in ETAOIN[:6]:
        if commonLetter in freqOrder[:6]:
            matchScore += 1
    # Find how many matches for the six least common letters there are.
    for uncommonLetter in ETAOIN[-6:]:
        if uncommonLetter in freqOrder[-6:]:
            matchScore += 1

    return matchScore
