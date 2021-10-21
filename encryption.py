from Crypto.Cipher import AES


# padding text to be multiple of 16 bytes
def pad_text(plaintext):
    elen = len(plaintext) % 16
    if elen:
        plaintext += bytes(16 - elen)
    return plaintext


def encrypt_with_ecb(plaintext, key):
    # divide padded plaintext into blocks
    blocks = []
    no_of_blocks = int(len(str(plaintext.hex())) / 32)
    for i in range(0, no_of_blocks * 32, 32):
        aux = plaintext.hex()[i:(32 + i)]
        aux2 = bytes.fromhex(aux)
        blocks.append(aux2)

    # starting encryption
    # we encrypt every block using predefined functions

    cipher_block = AES.new(key, AES.MODE_ECB)
    crypto_blocks = []
    for block in blocks:
        aux = cipher_block.encrypt(block)
        crypto_blocks.append(aux)

    # assembling ciphertext
    ciphertext = bytearray()
    for block in crypto_blocks:
        ciphertext += block

    # print("ciphertext hex is: ")
    # print(ciphertext.hex())
    # print("real ciphertext is:")
    # print(cipher_block.encrypt(plaintext).hex())
    return ciphertext


def xor_byte_array(arr1, arr2):
    arr1_as_bits = ''.join(format(byte, '08b') for byte in arr1)
    arr2_as_bits = ''.join(format(byte, '08b') for byte in arr2)

    xored_arr = ""
    for i in range(0, len(arr1_as_bits)):
        if arr1_as_bits[i] == arr2_as_bits[i]:
            xored_arr += "0"
        else:
            xored_arr += "1"

    hex_arr = "{0:#0{1}x}".format(int(xored_arr, 2), 34)
    xored_bytes = bytearray.fromhex(hex_arr[2:])

    return xored_bytes


def encrypt_with_cbc(plaintext, key, iv):
    # divide padded plaintext into blocks
    blocks = []
    no_of_blocks = int(len(str(plaintext.hex())) / 32)
    for i in range(0, no_of_blocks * 32, 32):
        aux = plaintext.hex()[i:(32 + i)]
        aux2 = bytes.fromhex(aux)
        blocks.append(aux2)

    cipher_block = AES.new(key, AES.MODE_ECB)
    crypto_blocks = []
    for i in range(0, no_of_blocks):
        if i == 0:
            aux_block = cipher_block.encrypt(xor_byte_array(blocks[i], iv))
            crypto_blocks.append(aux_block)
        else:
            aux_block = cipher_block.encrypt(xor_byte_array(blocks[i], crypto_blocks[-1]))
            crypto_blocks.append(aux_block)

    # assembling ciphertext
    ciphertext = bytearray()
    for block in crypto_blocks:
        ciphertext += block

    # print("ciphertext hex is: ")
    # print(ciphertext.hex())
    # print("real ciphertext is:")
    # cipher_block_2 = AES.new(key, AES.MODE_CBC, iv)
    # print(cipher_block_2.encrypt(plaintext).hex())
    return ciphertext
