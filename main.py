from KM import KM
from NodeA import NodeA
from NodeB import NodeB
import os


if __name__ == '__main__':
    k_prime = os.urandom(16)
    init_vector = os.urandom(16)
    print("K' and IV were generated...")

    nodeA = NodeA(k_prime, init_vector)
    nodeB = NodeB(k_prime, init_vector)
    km = KM(k_prime)

    encryption_type = input("Select the mode of operation for AES: ecb or cbc: ")
    if encryption_type != "ecb" and encryption_type != "cbc":
        raise NameError("You haven't selected a valid mode")

    nodeA.set_encryption_mode(encryption_type)
    nodeB.set_encryption_mode(encryption_type)

    encrypted_k = km.encrypt_k()

    print("A and B received encrypted K")
    nodeA.set_encrypted_k(encrypted_k)
    nodeB.set_encrypted_k(encrypted_k)

    nodeA.decrypt_k()
    nodeB.decrypt_k()

    print("A and B decrypted K...")

    print("A and B have started communicating...")

    nodeA.read_file()
    nodeA.encrypt_file()
    nodeA.write_file()
    print("A encrypted demofile.txt. Cryptotext is transmitted to B...")

    print("B received cryptotext. B is decrypting...")
    nodeB.read_file()
    nodeB.decrypt_file()
    nodeB.write_file()
    print("B decrypted the cryptotext and wrote it in decryption.txt")

    print()
    print("--------------------------------------------------------------------")
    print("Important values: ")
    print("--------------------------------------------------------------------")
    print("K is:")
    print(km.k.hex())
    print("K' is:")
    print(km.k_prime.hex())
    print("Initialization vector is:")
    print(nodeA.init_vector.hex())
    print("Plaintext is:")
    print(nodeA.plaintext.decode())
    print("Ciphertext is:")
    print(nodeA.ciphertext.hex())
    print("B decrypted ciphertext:")
    print(nodeB.plaintext)
