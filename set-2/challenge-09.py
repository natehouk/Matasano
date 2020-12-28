def pad(plaintext, blocksize):
    plaintext_bytes = bytes(plaintext, 'latin-1')
    padding = blocksize - len(plaintext_bytes) % blocksize
    if(padding == 16):
        padding = 0
    padded_bytes = plaintext_bytes
    for byte in range(0, padding):
        padded_bytes += b"\x04"
    assert len(padded_bytes) % blocksize == 0
    return padded_bytes

print(pad("YELLOW SUBMARINE", 20))