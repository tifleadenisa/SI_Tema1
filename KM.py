import os
from Crypto.Cipher import AES


class KM:
    k = os.urandom(16)
    encrypted_key = 0

    def __init__(self, k_prime):
        self.k_prime = k_prime

    # encrypt k using k'
    def encrypt_k(self):
        cipher = AES.new(self.k_prime, AES.MODE_ECB)
        msg = cipher.encrypt(self.k)
        # print("k string is")
        # print(self.k.hex())
        # print("k_prime string is")
        # print(self.k_prime.hex())
        # print("msg string is")
        # print(msg.hex())
        return msg
