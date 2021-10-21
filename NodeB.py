from Crypto.Cipher import AES

import decryption


class NodeB:
    k = 0
    file = ""
    encrypt_mode = ""
    encrypted_k = 0
    ciphertext = ""
    plaintext = ""

    def __init__(self, k_prime, init_vector):
        self.k_prime = k_prime
        self.init_vector = init_vector

    def set_encryption_mode(self, encrypt_mode):
        self.encrypt_mode = encrypt_mode

    def set_encrypted_k(self, encrypted_k):
        self.encrypted_k = encrypted_k

    def decrypt_k(self):
        plaintext = AES.new(self.k_prime, AES.MODE_ECB)
        self.k = plaintext.decrypt(self.encrypted_k)
        # print("Decrypted k is")
        # print(self.k.hex())

    def read_file(self):
        f = open("ciphertext.txt", "r")
        self.ciphertext = str.encode(f.read())
        # print(type(self.ciphertext))
        # print(self.ciphertext)

    def decrypt_file(self):
        if self.encrypt_mode == "ecb":
            self.plaintext = decryption.decrypt_with_ecb(self.ciphertext, self.k)
            print("B decrypted text with ECB")
        else:
            self.plaintext = decryption.decrypt_with_cbc(self.ciphertext, self.k, self.init_vector)
            print("B decrypted text with CBC")
        self.plaintext = self.plaintext.decode('ascii').strip().strip('\x00')
        # print(self.plaintext)

    def write_file(self):
        f = open("decryption.txt", "w")
        f.write(self.plaintext)
        f.close()
