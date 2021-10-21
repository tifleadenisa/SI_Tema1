from Crypto.Cipher import AES


def decrypt_with_ecb(ciphertext, key):
    # divide padded plaintext into blocks
    blocks = []
    no_of_blocks = int(len(ciphertext) / 32)
    for i in range(0, no_of_blocks * 32, 32):
        aux = ciphertext[i:(32 + i)]
        aux2 = aux.decode()
        blocks.append(bytes.fromhex(aux2))

    cipher_block = AES.new(key, AES.MODE_ECB)
    plaintext_blocks = []
    for block in blocks:
        aux = cipher_block.decrypt(block)
        plaintext_blocks.append(aux)

    # assembling plaintext
    plaintext = bytearray()
    for block in plaintext_blocks:
        plaintext += block

    # print("plaintext is")
    # print(plaintext)
    # print("plaintext in hex is:")
    # print(plaintext.hex())
    return plaintext


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


def decrypt_with_cbc(ciphertext, key, iv):
    # divide padded plaintext into blocks
    blocks = []
    no_of_blocks = int(len(ciphertext) / 32)
    for i in range(0, no_of_blocks * 32, 32):
        aux = ciphertext[i:(32 + i)]
        aux2 = aux.decode()
        blocks.append(bytes.fromhex(aux2))

    cipher_block = AES.new(key, AES.MODE_ECB)
    plaintext_blocks = []

    for i in range(0, no_of_blocks):
        if i == 0:
            plaintext_blocks.append(xor_byte_array(cipher_block.decrypt(blocks[i]), iv))
        else:
            plaintext_blocks.append(xor_byte_array(cipher_block.decrypt(blocks[i]), blocks[i-1]))

    plaintext = bytearray()
    for block in plaintext_blocks:
        plaintext += block

    # print("plaintext is")
    # print(plaintext)
    # print("plaintext in hex is:")
    # print(plaintext.hex())
    return plaintext
