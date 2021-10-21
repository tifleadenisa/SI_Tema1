from Crypto.Cipher import AES
import encryption


class NodeA:
    k = 0
    file = ""
    encrypt_mode = ""
    encrypted_k = 0
    plaintext = ""
    ciphertext = bytearray()

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

    def read_file(self):
        f = open("demofile.txt", "r")
        self.plaintext = str.encode(f.read())

    def write_file(self):
        f = open("ciphertext.txt", "w")
        f.write(self.ciphertext.hex())
        f.close()

    def encrypt_file(self):
        if self.encrypt_mode == "ecb":
            self.ciphertext = encryption.encrypt_with_ecb(encryption.pad_text(self.plaintext), self.k)
            print("A will send a text encrypted with ecb.")
        else:
            self.ciphertext = encryption.encrypt_with_cbc(encryption.pad_text(self.plaintext), self.k, self.init_vector)
            print("A will send a text encrypted with cbc.")
