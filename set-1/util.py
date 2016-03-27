import binascii
def hex2base64(hex):
    return(binascii.b2a_base64(hex.decode("hex"))[:-1])
