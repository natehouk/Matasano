import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Crypto.Cipher import AES
from util.util import xor, pad, encode_hex, encrypt_ecb, decrypt_ecb, bytes2hex
import base64

# Given constants
key = b"YELLOW SUBMARINE"
iv = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

# Given input file
filename = "files/input-10a.txt"

# Open file and read plaintext
with open(filename) as file:
    plaintext = file.read().replace("\n", "")

# Encrypt plaintext using ECB in CBC mode
ciphertext = b""
blocks = int(len(plaintext) / 16)
for i in range(0, blocks):
    block = plaintext[i * 16:(i + 1) * 16]
    block = xor(block, str(iv, 'latin-1'))
    encrypted_block = encrypt_ecb(key, pad(block, 16))
    ciphertext += encrypted_block
    iv = encrypted_block
print(ciphertext)

# Reset iv
iv = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

# Decrypt ciphertext using ECB in CBC mode
plaintext=b""
blocks = int(len(ciphertext) / 16)
for i in reversed(range(0, blocks)):
    if (i == 0):
        prev_block = str(iv, 'latin-1')
    else:
        prev_block = str(ciphertext[(i - 1) * 16:i * 16], 'latin-1')
    block = str(ciphertext[i * 16:(i + 1) * 16], 'latin-1')
    decrypted_block = decrypt_ecb(key, pad(block, 16))
    decrypted_block = xor(str(decrypted_block, 'latin-1'), prev_block)
    plaintext = bytes(decrypted_block, 'latin-1') + plaintext
print(str(plaintext, 'latin-1'))

#091230aade3eb330dbaa4358f88d2a6c37b72d0cf4c22c344aec4142d00ce530b181ceb5742ecf49b495dee7c71cc8ed302b23a133b9d861bece9fa3186610a6195dc11d49044951e80f10593d8fa8cb1bf2dca84330fb55c9a042e0f4592c45128864cd1d0e593467dbe6a63e58b2b776f5b4b1f79fd7a8ccbd3259e99154ae
#091230aade3eb330dbaa4358f88d2a6c091230aade3eb330dbaa4358f88d2a6c091230aade3eb330dbaa4358f88d2a6c091230aade3eb330dbaa4358f88d2a6c091230aade3eb330dbaa4358f88d2a6c091230aade3eb330dbaa4358f88d2a6c091230aade3eb330dbaa4358f88d2a6c
#091230AADE3EB330DBAA4358F88D2A6C37B72D0CF4C22C344AEC4142D00CE530B181CEB5742ECF49B495DEE7C71CC8ED302B23A133B9D861BECE9FA3186610A6195DC11D49044951E80F10593D8FA8CB1BF2DCA84330FB55C9A042E0F4592C45128864CD1D0E593467DBE6A63E58B2B7D7CBDCAE2D8227780F99FBC504CAFEB2
#091230aade3eb330dbaa4358f88d2a6c37b72d0cf4c22c344aec4142d00ce530b181ceb5742ecf49b495dee7c71cc8ed302b23a133b9d861bece9fa3186610a6195dc11d49044951e80f10593d8fa8cb1bf2dca84330fb55c9a042e0f4592c45128864cd1d0e593467dbe6a63e58b2b77e6c8de0f5ecfca925b725804f45469a
#091230aade3eb330dbaa4358f88d2a6c37b72d0cf4c22c344aec4142d00ce530b181ceb5742ecf49b495dee7c71cc8ed302b23a133b9d861bece9fa3186610a6195dc11d49044951e80f10593d8fa8cb1bf2dca84330fb55c9a042e0f4592c45128864cd1d0e593467dbe6a63e58b2b776f5b4b1f79fd7a8ccbd3259e99154ae 6efb778817117197df3f42f969bc7bba4200acb1f4fdaf78774fd479c2543beff7737bac5fd22b0e5f338b1fe73df639c6d1e5303fa4aad7a5fbf8f436d7103e8593e591528de138ab7b743a7eb05a75eae924443411d7be74ecd0699ef18e69e42fcc6f78cea59c3de256efcdf8383a9b1bacfc687ba21c44b825431e4c0dc0db335e9261362b796a678d6daf0a66b776b4c275d86c9cf5f7a6a5f48f86ff4dbc8920a010c0d08468bc615bde085211980fc5ecc4cf1084390a1511a3932cd80955b7e1a384d2129714606cb216dc1e273358cba6ad895b00036acee7ce362d6ff620d48c428bacd7231de149596f61af97d392b47ca6447349d21d09b9ffc63d407770aaf4abcacb2af282a572f879af2f71aaea2d062abe248598fc39d3392c4de4dc36cfe4e98b607986795fc45e5c2d4a41b364f9258b64455be299be3aa9a3afec21e6b7607c0bdfe52808fc22eac49282a5b3dcba20eb092f8bd968078a95292e4d8906af4f412da1eaf1985b0df4a2f78811d4b267cfbdde70222e3d
#091230aade3eb330dbaa4358f88d2a6c37b72d0cf4c22c344aec4142d00ce530b181ceb5742ecf49b495dee7c71cc8ed302b23a133b9d861bece9fa3186610a6195dc11d49044951e80f10593d8fa8cb1bf2dca84330fb55c9a042e0f4592c45128864cd1d0e593467dbe6a63e58b2b776f5b4b1f79fd7a8ccbd3259e99154ae f89b0f96b835b72441a366f1b68ef6d3cc95f3998c15652a05066efab484d15b97fc2bfe8186b0e42a94e9f18ea360bad039a0379222b8e2acc3ef1628741481b1ae8f79bdaafeea64f2bc0853c228b19493e2d2d66de8b9d9e0a93645cb43ada497fe98b29ca9758b8c8001d6d188a2f3ecc9aab96c1eb51d6460197037bc5f6353fd3eb1d41353656409e5ea59aefe8dec7c4bbea3ed8adbac330845b64840c710dc91c822d81af4894796256dabf428ad51d259fad1e1331bed6d1f71a3663dd08aaa5fb0ebc885f41f01140a549e321d2d38aebd3e1b881f6875e7d0a556bf0f921f32823c978f42eb87313968b36613f4f78e0794f42e05a5b728d09a7724c883f9406fa3b0e6b15723912809c17c4b76f053707ae096e015c373bb0a794b23c20d0920549381bbd65e77d30f3a82cbbf4ba11ba75cf5da593a9fb0f47fa29e169d58a218d011dd8241ae5df8266d4d0dc34eb378f327f5c8e3007d34a2b8024fddd31bb561fc15753a0461b9e5bf9fa2e106caea80d0164ac6e7ec6cf8